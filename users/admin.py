from django.contrib import admin

from .models import ProductSuggestion, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for user profiles."""

    list_display = (
        "user",
        "default_full_name",
        "default_email",
    )
    search_fields = (
        "user__username",
        "user__email",
        "default_full_name",
        "default_email",
    )


@admin.register(ProductSuggestion)
class ProductSuggestionAdmin(admin.ModelAdmin):
    """Admin configuration for product suggestions."""

    list_display = (
        "suggested_name",
        "user",
        "suggested_category",
        "status",
        "created_on",
        "updated_on",
    )
    list_filter = (
        "status",
        "suggested_category",
        "created_on",
        "updated_on",
    )
    search_fields = (
        "suggested_name",
        "suggested_category",
        "description",
        "reason",
        "reference_url",
        "user__username",
        "user__email",
    )
    readonly_fields = (
        "created_on",
        "updated_on",
    )
    ordering = ("-created_on",)
