import json
import time

from django.http import HttpResponse

from products.models import Product
from users.models import UserProfile

from .models import Order, OrderLineItem


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

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook."""
        intent = event.data.object
        pid = intent.id

        bag = json.loads(intent.metadata.get("bag", "{}"))
        username = intent.metadata.get("username", "AnonymousUser")

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                Order.objects.get(payment_intent_id=pid)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f"Webhook received: {event['type']} | SUCCESS",
                status=200,
            )

        if not bag:
            return HttpResponse(
                content=(
                    f"Webhook received: {event['type']} | "
                    "No bag metadata found"
                ),
                status=200,
            )

        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
        else:
            profile = None

        order = None

        try:
            order = Order.objects.create(
                full_name="Webhook Customer",
                email="webhook@example.com",
                payment_intent_id=pid,
                bag_snapshot=json.dumps(bag),
                user_profile=profile,
            )

            for item_id, quantity in bag.items():
                product = Product.objects.get(pk=item_id)
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                )

        except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
                content=f"Webhook error: {e}",
                status=500,
            )

        return HttpResponse(
            content=f"Webhook received: {event['type']} | SUCCESS",
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook."""
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200,
        )
