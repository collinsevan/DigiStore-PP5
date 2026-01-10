from django.shortcuts import render
from django.shortcuts import redirect


def view_bag(request):
    """A view to return the shopping bag page."""
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    bag = request.session.get("bag", {})

    item_id = str(item_id)

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session["bag"] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product in the bag."""
    quantity = int(request.POST.get("quantity"))
    bag = request.session.get("bag", {})
    item_id = str(item_id)

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id, None)

    request.session["bag"] = bag
    return redirect("view_bag")


def remove_from_bag(request, item_id):
    """Remove the specified product from the bag."""
    bag = request.session.get("bag", {})
    item_id = str(item_id)

    bag.pop(item_id, None)
    request.session["bag"] = bag
    return redirect("view_bag")
