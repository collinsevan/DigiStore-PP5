from django.shortcuts import render


from .models import Product


def all_products(request):
    """
    Display all products.

    Intended to support sorting and searching in future iterations.
    """
    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)
