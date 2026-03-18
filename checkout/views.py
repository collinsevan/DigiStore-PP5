import json
from decimal import Decimal

import stripe
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.http import require_POST

from bag.contexts import bag_contents
from products.models import Product
from users.models import UserProfile

from .forms import OrderForm
from .models import Order, OrderLineItem


@require_POST
def cache_checkout_data(request):
    """Cache checkout data in the Stripe PaymentIntent metadata."""
    try:
        data = json.loads(request.body)
        client_secret = data.get("client_secret")
        pid = client_secret.split("_secret")[0]

        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": str(data.get("save_info")),
                "username": (
                    request.user.username
                    if request.user.is_authenticated
                    else "AnonymousUser"
                ),
            },
        )
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now."
        )
        return HttpResponse(
            content=str(e),
            status=400
        )


def checkout(request):
    """Process checkout, create order, and prepare Stripe payment."""
    bag = request.session.get("bag", {})

    """Prevent checkout if the shopping bag is empty."""
    if not bag:
        messages.info(request, "Your bag is empty.")
        return redirect(reverse("view_bag"))

    """Handle order submission when the checkout form is posted."""
    if request.method == "POST":
        client_secret = request.POST.get("client_secret", "")

        """Ensure Stripe payment intent exists before processing."""
        if not client_secret:
            messages.error(
                request,
                "Payment was not confirmed. Please try again."
            )
            return redirect(reverse("checkout"))

        pid = client_secret.split("_secret")[0]

        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)

            """Attach Stripe payment intent and bag snapshot."""
            order.payment_intent_id = pid
            order.bag_snapshot = json.dumps(bag)

            """Link order to authenticated user profile."""
            if request.user.is_authenticated:
                profile, _ = UserProfile.objects.get_or_create(
                    user=request.user
                )
                order.user_profile = profile

            order.save()

            """Store save_info choice in the session."""
            request.session["save_info"] = "save_info" in request.POST

            """Create line items for each product stored in bag."""
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(pk=item_id)
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=int(quantity),
                    )
                except Product.DoesNotExist:
                    """Delete incomplete order if a product is missing."""
                    messages.error(
                        request,
                        "One of the products in your bag was not found."
                    )
                    order.delete()
                    return redirect(reverse("view_bag"))

            return redirect(
                reverse(
                    "checkout_success",
                    args=[order.reference]
                )
            )

        """Show an error if the submitted order form is invalid."""
        messages.error(
            request,
            "There was an error with your form. Please check your details."
        )

    """Prepare order form and totals for checkout page."""
    order_form = OrderForm()
    context = bag_contents(request)
    grand_total = context.get("grand_total", Decimal("0.00"))

    """Create Stripe PaymentIntent using order total."""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=int(grand_total * 100),
        currency=settings.STRIPE_CURRENCY,
    )

    """Warn if the Stripe public key is missing."""
    if not settings.STRIPE_PUBLIC_KEY:
        messages.warning(
            request,
            "Stripe public key is missing. Did you forget to set it?"
        )

    """Add form and Stripe keys to template context."""
    context["order_form"] = order_form
    context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
    context["client_secret"] = intent.client_secret

    return render(request, "checkout/checkout.html", context)


def checkout_success(request, reference):
    """Display confirmation page and clear the bag."""

    """Get the saved profile preference from the session."""
    save_info = request.session.get("save_info")

    """Retrieve the completed order by its reference."""
    order = get_object_or_404(Order, reference=reference)

    messages.success(
        request,
        f"Order successfully created: {reference}. "
        f"A confirmation will be sent to {order.email}."
    )
    request.session.pop("bag", None)

    return render(
        request,
        "checkout/checkout_success.html",
        {
            "order": order,
            "save_info": save_info,
        },
    )
