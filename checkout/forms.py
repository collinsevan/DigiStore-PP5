from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Collects customer details for an order."""

    class Meta:
        model = Order
        fields = ("full_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Full name"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email address"}
        )
