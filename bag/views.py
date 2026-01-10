from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404

from products.models import Product


def view_bag(request):
    """A view to return the shopping bag page."""
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the bag."""
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get("quantity", 1))
    redirect_url = request.POST.get("redirect_url")

    bag = request.session.get("bag", {})
    item_id = str(item_id)

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session["bag"] = bag

    messages.success(request, f"Added {product.name} to your bag.")
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product in the bag."""
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get("quantity", 1))
    bag = request.session.get("bag", {})
    item_id = str(item_id)

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f"Updated {product.name} quantity to {quantity}.")
    else:
        bag.pop(item_id, None)
        messages.success(request, f"Removed {product.name} from your bag.")

    request.session["bag"] = bag
    return redirect("view_bag")


def remove_from_bag(request, item_id):
    """Remove the specified product from the bag (AJAX endpoint)."""
    try:
        product = get_object_or_404(Product, pk=item_id)

        bag = request.session.get("bag", {})
        item_id = str(item_id)

        bag.pop(item_id, None)
        request.session["bag"] = bag

        messages.success(request, f"Removed {product.name} from your bag.")
        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)
