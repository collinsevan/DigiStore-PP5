from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for product categories.
    """
    list_display = (
        "friendly_name",
        "name",
        "slug",
    )
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for products.
    """
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "license_type",
        "is_digital",
    )
    ordering = ("sku",)
