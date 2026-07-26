from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("faq/", views.faq, name="faq"),
    path(
        "newsletter/subscribe/",
        views.newsletter_subscribe,
        name="newsletter_subscribe",
    ),
]
