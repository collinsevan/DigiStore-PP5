from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile defaults."""

    class Meta:
        model = UserProfile
        fields = (
            "default_full_name",
            "default_email",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "default_full_name": "Full name",
            "default_email": "Email address",
        }

        for field_name, field in self.fields.items():
            field.widget.attrs["placeholder"] = placeholders[field_name]
            field.widget.attrs["class"] = "form-control rounded-0"
            field.label = field.label
