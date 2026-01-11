import json

from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from bag.contexts import bag_contents
from products.models import Product

from .forms import OrderForm
from .models import OrderLineItem


def checkout(request):
    """Create an order from bag contents and render checkout."""
    bag = request.session.get("bag", {})

    if not bag:
        messages.info(request, "Your bag is empty.")
        return redirect(reverse("bag:view_bag"))

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.bag_snapshot = json.dumps(bag)
            order.save()

            for item_id, quantity in bag.items():
                product = Product.objects.get(pk=item_id)
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=int(quantity),
                )

            return redirect(reverse("checkout:checkout_success", args=[order.reference]))

    order_form = OrderForm()
    context = bag_contents(request)
    context["order_form"] = order_form
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
