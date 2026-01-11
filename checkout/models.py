import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.utils import timezone

from products.models import Product


class Order(models.Model):
    """Stores a completed checkout order."""

    class Status(models.TextChoices):
        CREATED = "CREATED", "Created"
        PAID = "PAID", "Paid"
        FAILED = "FAILED", "Failed"
        REFUNDED = "REFUNDED", "Refunded"

    reference = models.CharField(max_length=20, unique=True, editable=False)

    full_name = models.CharField(max_length=80)
    email = models.EmailField()

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.CREATED,
    )

    payment_intent_id = models.CharField(
        max_length=255, blank=True, default="")
    bag_snapshot = models.TextField(blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        editable=False,
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        editable=False,
    )

    confirmation_email_sent = models.BooleanField(default=False)

    def _generate_reference(self):
        """Create a readable order reference."""
        date_part = timezone.localdate().strftime("%Y%m%d")
        rand_part = uuid.uuid4().hex[:6].upper()
        return f"DS-{date_part}-{rand_part}"

    def update_totals(self):
        """Recalculate totals from related line items."""
        self.order_total = (
            self.lineitems.aggregate(Sum("line_total"))["line_total__sum"]
            or Decimal("0.00")
        )
        self.grand_total = self.order_total
        self.save(update_fields=["order_total", "grand_total", "updated_at"])

    def save(self, *args, **kwargs):
        """Set reference once and keep it stable."""
        if not self.reference:
            ref = self._generate_reference()
            while Order.objects.filter(reference=ref).exists():
                ref = self._generate_reference()
            self.reference = ref
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference


class OrderLineItem(models.Model):
    """A purchased product within an order (price/licence snapshot)."""

    order = models.ForeignKey(
        Order,
        related_name="lineitems",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=254, editable=False)
    sku = models.CharField(max_length=254, blank=True,
                           default="", editable=False)
    purchased_license_type = models.CharField(
        max_length=20,
        blank=True,
        default="",
        editable=False,
    )

    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        default=0,
    )
    line_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        default=0,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Snapshot product fields and compute totals for this line."""
        self.product_name = self.product.name
        self.sku = self.product.sku or ""
        self.purchased_license_type = self.product.license_type

        self.unit_price = self.product.price
        self.line_total = self.unit_price * self.quantity

        super().save(*args, **kwargs)
        self.order.update_totals()

    def __str__(self):
        return f"{self.quantity} x {self.product_name} ({self.order.reference})"
