from django.shortcuts import render


def index(request):
    """Return the home page."""
    return render(request, "marketing/index.html")


def faq(request):
    """Return the FAQ page."""
    return render(request, "marketing/faq.html")
