from django.contrib import admin
from .models import Category, Product, PromoCode


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


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    """
    Admin configuration for promo codes.
    """
    list_display = (
        "code",
        "discount_type",
        "discount_value",
        "is_active",
        "valid_from",
        "valid_to",
    )
    list_filter = (
        "discount_type",
        "is_active",
    )
    search_fields = (
        "code",
        "description",
    )
    ordering = ("code",)
