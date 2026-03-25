from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Form for store owners to create and update products."""

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

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
