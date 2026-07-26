from django.contrib import admin
from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "subscribed_on",
        "is_active",
    )

    search_fields = (
        "email",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "-subscribed_on",
    )
