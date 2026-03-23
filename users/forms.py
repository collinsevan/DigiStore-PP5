from django import forms

from .models import UserProfile


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
