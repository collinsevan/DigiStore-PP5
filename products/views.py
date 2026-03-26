from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .forms import ProductForm
from .models import Product, Category


def all_products(request):
    """
    Display all products.

    Supports:
    - Search queries via ?q=
    - Category filtering via ?category=
    - Sorting via ?sort=&direction=
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET.get("q")

            if not query:
                messages.error(
                    request, "You didn't enter any search criteria.")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        if "category" in request.GET:
            category_slug = request.GET.get("category")
            categories = Category.objects.filter(slug=category_slug)
            products = products.filter(category__in=categories)

        if "sort" in request.GET:
            sort = request.GET.get("sort")
            sortkey = sort

            if sortkey == "name":
                products = products.annotate(lower_name=Lower("name"))
                sortkey = "lower_name"

            if sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                direction = request.GET.get("direction")

            if direction == "desc":
                sortkey = f"-{sortkey}"

            products = products.order_by(sortkey)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
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


@login_required
def add_product(request):
    """
    Add a product to the store.
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, only store owners can do that."
        )
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            messages.success(request, "Product added successfully.")
            return redirect(
                reverse("product_detail", args=[product.id])
            )

        messages.error(
            request,
            "Failed to add product. Please ensure the form is valid."
        )

    else:
        form = ProductForm()

    context = {
        "form": form,
    }

    return render(request, "products/add_product.html", context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store.
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, only store owners can do that."
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect(
                reverse("product_detail", args=[product.id])
            )

        messages.error(
            request,
            "Failed to update product. Please ensure the form is valid."
        )

    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    context = {
        "form": form,
        "product": product,
    }

    return render(request, "products/edit_product.html", context)
