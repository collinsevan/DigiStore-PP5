from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks."""

    def __init__(self, request):
        """Store the request sent by Stripe."""
        self.request = request

    def handle_event(self, event):
        """Handle a generic or unexpected webhook event."""
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )
