from django.shortcuts import render, get_object_or_404

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


def product_detail(request, product_id):
    """
    Display an individual product.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product-detail.html", context)
