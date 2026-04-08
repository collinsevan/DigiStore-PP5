from django.shortcuts import render


def custom_401(request):
    """Render custom 401 page."""
    return render(request, "errors/401.html", status=401)


def custom_403(request):
    """Render custom 403 page."""
    return render(request, "errors/403.html", status=403)


def custom_404(request):
    """Render custom 404 page."""
    return render(request, "errors/404.html", status=404)


def custom_405(request):
    """Render custom 405 page."""
    return render(request, "errors/405.html", status=405)


def custom_408(request):
    """Render custom 408 page."""
    return render(request, "errors/408.html", status=408)


def custom_429(request):
    """Render custom 429 page."""
    return render(request, "errors/429.html", status=429)


def custom_502(request):
    """Render custom 502 page."""
    return render(request, "errors/502.html", status=502)


def custom_503(request):
    """Render custom 503 page."""
    return render(request, "errors/503.html", status=503)


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
