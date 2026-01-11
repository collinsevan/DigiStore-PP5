from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """Checkout form for customer details."""

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "full_name": "Full name",
            "email": "Email address",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True

        for field_name, field in self.fields.items():
            placeholder = placeholders.get(field_name, "")

            if field.required and placeholder:
                placeholder = f"{placeholder} *"

            field.widget.attrs["placeholder"] = placeholder
            field.widget.attrs["class"] = "stripe-style-input"
            field.label = False
