from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """Return bag totals for use across the site"""
    bag_items = []
    total = 0
    product_count = 0
    grand_total = total

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "grand_total": grand_total,
    }

    return context
