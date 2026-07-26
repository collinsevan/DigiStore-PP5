from .forms import NewsletterSubscriptionForm


def newsletter_form(request):
    """
    Makes the newsletter subscription form
    available to all templates.
    """
    return {
        "newsletter_form": NewsletterSubscriptionForm()
    }
