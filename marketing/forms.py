from django import forms
from .models import NewsletterSubscriber


class NewsletterSubscriptionForm(forms.ModelForm):
    """
    Form used to subscribe users to the DigiStore newsletter.
    """

    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your email address",
                    "aria-label": "Email address",
                }
            ),
        }
