from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """Store default checkout details for a user."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    default_full_name = models.CharField(
        max_length=80,
        blank=True,
    )
    default_email = models.EmailField(
        max_length=254,
        blank=True,
    )

    def __str__(self):
        """Return the profile username."""
        return self.user.username


class ProductSuggestion(models.Model):
    """Store product suggestions submitted by authenticated users."""

    STATUS_PENDING = "pending"
    STATUS_UNDER_REVIEW = "under_review"
    STATUS_APPROVED = "approved"
    STATUS_DECLINED = "declined"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_UNDER_REVIEW, "Under Review"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_DECLINED, "Declined"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product_suggestions",
    )
    suggested_name = models.CharField(
        max_length=254,
    )
    suggested_category = models.CharField(
        max_length=254,
        blank=True,
    )
    description = models.TextField()
    reason = models.TextField(
        blank=True,
    )
    reference_url = models.URLField(
        max_length=1024,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    admin_notes = models.TextField(
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Product Suggestion"
        verbose_name_plural = "Product Suggestions"

    def __str__(self):
        """Return a readable product suggestion label."""
        return f"{self.suggested_name} ({self.user.username})"


@receiver(post_save, sender=get_user_model())
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user's profile after save."""
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)
        instance.profile.save()
