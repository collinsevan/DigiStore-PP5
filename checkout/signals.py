from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_delete, sender=OrderLineItem)
def update_order_totals_on_delete(sender, instance, **kwargs):
    """Update order totals after a line item is deleted."""
    instance.order.update_totals()
