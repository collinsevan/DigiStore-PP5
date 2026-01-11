import json
from decimal import Decimal

import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from bag.contexts import bag_contents
from products.models import Product

from .forms import OrderForm
from .models import OrderLineItem


def checkout(request):
    """Create an order after payment confirmation and render checkout."""
    bag = request.session.get("bag", {})

    if not bag:
        messages.info(request, "Your bag is empty.")
        return redirect(reverse("bag:view_bag"))

    if request.method == "POST":
        client_secret = request.POST.get("client_secret", "")

        if not client_secret:
            messages.error(
                request, "Payment was not confirmed. Please try again.")
            return redirect(reverse("checkout"))

        pid = client_secret.split("_secret")[0]

        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.payment_intent_id = pid
            order.bag_snapshot = json.dumps(bag)
            order.save()

            for item_id, quantity in bag.items():
                product = Product.objects.get(pk=item_id)
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=int(quantity),
                )

            return redirect(reverse("checkout_success", args=[order.reference]))

    order_form = OrderForm()
    context = bag_contents(request)
    grand_total = context.get("grand_total", Decimal("0.00"))

    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=int(grand_total * 100),
        currency=settings.STRIPE_CURRENCY,
    )

    context["order_form"] = order_form
    context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
    context["client_secret"] = intent.client_secret

    return render(request, "checkout/checkout.html", context)


def checkout_success(request, reference):
    """Display order confirmation and clear the bag."""
    messages.success(request, f"Order successfully created: {reference}")
    request.session.pop("bag", None)

    return render(
        request,
        "checkout/checkout_success.html",
        {"reference": reference},
    )
