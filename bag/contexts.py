from decimal import Decimal
from django.shortcuts import get_object_or_404

from products.models import Product


def bag_contents(request):
    """Return bag totals and items for use across the site."""
    bag_items = []
    total = Decimal("0.00")
    product_count = 0

    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(quantity)

        line_total = quantity * product.price
        total += line_total
        product_count += quantity

        bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
                "line_total": line_total,
            }
        )

    grand_total = total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "grand_total": grand_total,
    }

    return context
