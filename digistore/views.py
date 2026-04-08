from django.shortcuts import render


def custom_401(request):
    """Render custom 401 page."""
    return render(request, "errors/401.html", status=401)


def handler400(request, exception):
    """Render custom 400 page."""
    return render(request, "errors/400.html", status=400)


def handler403(request, exception):
    """Render custom 403 page."""
    return render(request, "errors/403.html", status=403)


def handler404(request, exception):
    """Render custom 404 page."""
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """Render custom 500 page."""
    return render(request, "errors/500.html", status=500)
