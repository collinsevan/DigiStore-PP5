from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Product category used for grouping and navigation.
    """

    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=254, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """
    Digital product available for purchase.
    """

    LICENSE_PERSONAL = "personal"
    LICENSE_COMMERCIAL = "commercial"
    LICENSE_EXTENDED = "extended"

    LICENSE_CHOICES = [
        (LICENSE_PERSONAL, "Personal"),
        (LICENSE_COMMERCIAL, "Commercial"),
        (LICENSE_EXTENDED, "Extended"),
    ]

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="products",
    )

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True, blank=True)

    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True,
    )

    is_digital = models.BooleanField(default=True)
    license_type = models.CharField(
        max_length=20,
        choices=LICENSE_CHOICES,
        default=LICENSE_PERSONAL,
    )

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
