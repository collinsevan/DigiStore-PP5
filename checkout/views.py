import json
from decimal import Decimal

import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from bag.contexts import bag_contents
from products.models import Product
from users.models import UserProfile

from .forms import OrderForm
from .models import OrderLineItem


def checkout(request):
    """Process checkout, create order, and prepare Stripe payment."""
    bag = request.session.get("bag", {})

    """Prevent checkout if the shopping bag is empty."""
    if not bag:
        messages.info(request, "Your bag is empty.")
        return redirect(reverse("bag:view_bag"))

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

            """Create line items for each product stored in bag."""
            for item_id, quantity in bag.items():
                product = Product.objects.get(pk=item_id)
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=int(quantity),
                )

            return redirect(
                reverse(
                    "checkout_success",
                    args=[order.reference]
                )
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

    """Add form and Stripe keys to template context."""
    context["order_form"] = order_form
    context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
    context["client_secret"] = intent.client_secret

    return render(request, "checkout/checkout.html", context)


def checkout_success(request, reference):
    """Display confirmation page and clear the bag."""
    messages.success(
        request,
        f"Order successfully created: {reference}"
    )
    request.session.pop("bag", None)

    return render(
        request,
        "checkout/checkout_success.html",
        {"reference": reference},
    )
