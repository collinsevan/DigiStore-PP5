from django.shortcuts import render


def custom_401(request):
    """Render custom 401 page."""
    return render(request, "errors/401.html", status=401)
