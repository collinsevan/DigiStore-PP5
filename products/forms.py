from django import forms

from .models import Category, Product, ProductBadge, PromoCode
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """Form for store owners to create and update products."""

    image = forms.ImageField(
        label="Image",
        required=False,
        widget=CustomClearableFileInput(
            attrs={"id": "new-image"}
        ),
    )

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """Customise form fields."""
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names = [
            (c.id, c.get_friendly_name() or c.name) for c in categories
        ]

        self.fields["category"].choices = friendly_names

        badges = ProductBadge.objects.filter(is_active=True)
        badge_choices = [("", "---------")] + [
            (badge.id, badge.name) for badge in badges
        ]
        self.fields["badge"].choices = badge_choices

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class PromoCodeForm(forms.ModelForm):
    """Form for store owners to create and update promo codes."""

    class Meta:
        model = PromoCode
        fields = (
            "code",
            "description",
            "discount_type",
            "discount_value",
            "is_active",
            "valid_from",
            "valid_to",
        )

    def __init__(self, *args, **kwargs):
        """Customise form fields."""
        super().__init__(*args, **kwargs)

        self.fields["valid_from"].required = False
        self.fields["valid_to"].required = False

        self.fields["valid_from"].widget = forms.DateTimeInput(
            attrs={
                "class": "border-black rounded-0",
                "type": "datetime-local",
            },
            format="%Y-%m-%dT%H:%M",
        )
        self.fields["valid_to"].widget = forms.DateTimeInput(
            attrs={
                "class": "border-black rounded-0",
                "type": "datetime-local",
            },
            format="%Y-%m-%dT%H:%M",
        )

        for field_name, field in self.fields.items():
            if field_name not in ("valid_from", "valid_to"):
                existing_class = field.widget.attrs.get("class", "")
                field.widget.attrs["class"] = (
                    f"{existing_class} border-black rounded-0".strip()
                )

        if self.instance and self.instance.valid_from:
            self.initial["valid_from"] = self.instance.valid_from.strftime(
                "%Y-%m-%dT%H:%M"
            )

        if self.instance and self.instance.valid_to:
            self.initial["valid_to"] = self.instance.valid_to.strftime(
                "%Y-%m-%dT%H:%M"
            )
