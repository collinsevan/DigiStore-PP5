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
        "saved-searches/<int:saved_search_id>/edit/",
        views.edit_saved_search,
        name="edit_saved_search",
    ),
    path(
        "saved-searches/<int:saved_search_id>/delete/",
        views.delete_saved_search,
        name="delete_saved_search",
    ),
    path(
        "support-tickets/<int:ticket_id>/edit/",
        views.edit_support_ticket,
        name="edit_support_ticket",
    ),
    path(
        "support-tickets/<int:ticket_id>/delete/",
        views.delete_support_ticket,
        name="delete_support_ticket",
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
