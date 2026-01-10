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

    # Temporary test like the transcript (remove later)
    print("BAG:", request.session.get("bag"))

    return redirect(redirect_url)
