from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("success/<reference>/", views.checkout_success, name="checkout_success"),
]
