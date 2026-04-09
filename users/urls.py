from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path(
        "order_history/<reference>/",
        views.order_history,
        name="order_history",
    ),
    path(
        "suggestions/<int:suggestion_id>/edit/",
        views.edit_product_suggestion,
        name="edit_product_suggestion",
    ),
    path(
        "suggestions/<int:suggestion_id>/delete/",
        views.delete_product_suggestion,
        name="delete_product_suggestion",
    ),
]
