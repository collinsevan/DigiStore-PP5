from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Inline line items on the order admin page."""

    model = OrderLineItem
    extra = 0
    can_delete = False
    readonly_fields = (
        "product",
        "product_name",
        "sku",
        "purchased_license_type",
        "quantity",
        "unit_price",
        "line_total",
        "created_at",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for viewing and searching orders."""

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "reference",
        "payment_intent_id",
        "bag_snapshot",
        "created_at",
        "updated_at",
        "order_total",
        "grand_total",
        "confirmation_email_sent",
    )

    fields = (
        "reference",
        "status",
        "full_name",
        "email",
        "payment_intent_id",
        "created_at",
        "updated_at",
        "order_total",
        "grand_total",
        "confirmation_email_sent",
        "bag_snapshot",
    )

    list_display = (
        "reference",
        "created_at",
        "full_name",
        "email",
        "status",
        "order_total",
        "grand_total",
    )

    ordering = ("-created_at",)
    search_fields = ("reference", "full_name", "email", "payment_intent_id")
