from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import NewsletterSubscriptionForm
from .models import NewsletterSubscriber


def index(request):
    """Return the home page."""
    return render(request, "marketing/index.html")


def faq(request):
    """Return the FAQ page."""
    return render(request, "marketing/faq.html")


def newsletter_subscribe(request):
    """
    Subscribe a user to the DigiStore newsletter.
    """
    if request.method == "POST":
        form = NewsletterSubscriptionForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            if NewsletterSubscriber.objects.filter(email=email).exists():
                messages.info(
                    request,
                    "This email is already subscribed to our newsletter."
                )
            else:
                # Save the subscriber
                subscriber = form.save()

                # Generate the welcome email
                email_body = render_to_string(
                    "marketing/emails/welcome_email.txt"
                )

                # Send the welcome email
                send_mail(
                    subject="Welcome to the DigiStore Newsletter!",
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[subscriber.email],
                    fail_silently=False,
                )

                messages.success(
                    request,
                    "Thank you for subscribing! "
                    "Please check your email for a welcome message."
                )

        else:
            for error in form.errors.get("email", []):
                messages.error(request, error)

        return redirect(request.META.get("HTTP_REFERER", "/"))

    return redirect("/")
