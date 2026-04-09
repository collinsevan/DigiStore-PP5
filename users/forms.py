from django import forms

from .models import ProductSuggestion, UserProfile


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile defaults."""

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "default_full_name": "Full name",
            "default_email": "Email address",
        }

        self.fields["default_full_name"].widget.attrs["autofocus"] = True

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(
                field_name, ""
            )
            field.widget.attrs["class"] = "form-control rounded-0"
            field.label = False


class ProductSuggestionForm(forms.ModelForm):
    """Form for users to submit product suggestions."""

    class Meta:
        model = ProductSuggestion
        fields = (
            "suggested_name",
            "suggested_category",
            "description",
            "reason",
            "reference_url",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "suggested_name": "Suggested product name",
            "suggested_category": "Suggested category",
            "description": "Describe the product idea",
            "reason": "Why should DigiStore add this product?",
            "reference_url": "Reference URL (optional)",
        }

        self.fields["suggested_name"].widget.attrs["autofocus"] = True

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders.get(
                field_name, ""
            )
            field.widget.attrs["class"] = "form-control rounded-0"

        self.fields["description"].widget.attrs["rows"] = 4
        self.fields["reason"].widget.attrs["rows"] = 4
