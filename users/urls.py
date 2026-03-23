from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path(
        "order_history/<reference>/",
        views.order_history,
        name="order_history",
    ),
]
