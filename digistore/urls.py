"""digistore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Import an Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path("", include("marketing.urls")),
    path("accounts/", include("allauth.urls")),
    path("bag/", include("bag.urls")),
    path("checkout/", include("checkout.urls")),
    path("users/", include("users.urls")),

    # Manual preview routes for custom error pages
    path("401/", views.custom_401, name="custom_401"),
    path("403/", views.custom_403, name="custom_403"),
    path("404/", views.custom_404, name="custom_404"),
    path("405/", views.custom_405, name="custom_405"),
    path("408/", views.custom_408, name="custom_408"),
    path("429/", views.custom_429, name="custom_429"),
    path("502/", views.custom_502, name="custom_502"),
    path("503/", views.custom_503, name="custom_503"),
]

handler400 = "digistore.views.handler400"
handler403 = "digistore.views.handler403"
handler404 = "digistore.views.handler404"
handler500 = "digistore.views.handler500"

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
