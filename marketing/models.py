from django.db import models


class NewsletterSubscriber(models.Model):
    """
    Stores newsletter subscribers for DigiStore marketing emails.
    """

    email = models.EmailField(
        unique=True,
        help_text="Subscriber email address."
    )

    subscribed_on = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Whether the subscriber is currently subscribed."
    )

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-subscribed_on"]
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"
