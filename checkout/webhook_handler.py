import json
import time
from decimal import Decimal

import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from products.models import Product
from users.models import UserProfile

from .models import Order, OrderLineItem


class StripeWH_Handler:
    """Handle Stripe webhooks."""

    def __init__(self, request):
        """Store the request sent by Stripe."""
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email for their order."""
        customer_email = order.email

        subject = render_to_string(
            "checkout/confirmation_email_subject.txt",
            {"order": order},
        ).strip()

        body = render_to_string(
            "checkout/confirmation_email_body.txt",
            {
                "order": order,
                "contact_email": settings.DEFAULT_FROM_EMAIL,
            },
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
        )

    def handle_event(self, event):
        """Handle a generic or unexpected webhook event."""
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Create the order from Stripe metadata if it does not already exist,
        then verify Stripe's charged total matches the order total.
        """
        intent = event.data.object
        pid = intent.id

        bag_data = intent.metadata.get("bag")
        if not bag_data:
            return HttpResponse(
                content="Webhook error: bag metadata missing",
                status=500,
            )

        bag = json.loads(bag_data)
        bag_snapshot = json.dumps(bag)
        save_info = intent.metadata.get("save_info", "False")
        username = intent.metadata.get("username", "AnonymousUser")

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        grand_total = Decimal(str(stripe_charge.amount / 100))

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    payment_intent_id=pid,
                    bag_snapshot=bag_snapshot,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f"Webhook verified order already exists: {event['type']}"
                ),
                status=200,
            )

        profile = None

        if username != "AnonymousUser":
            try:
                profile = UserProfile.objects.get(user__username=username)

                if save_info.lower() == "true":
                    profile.default_full_name = billing_details.name or ""
                    profile.default_email = billing_details.email or ""
                    profile.save()

            except UserProfile.DoesNotExist:
                profile = None

        order = None

        try:
            order = Order.objects.create(
                user_profile=profile,
                full_name=billing_details.name,
                email=billing_details.email,
                payment_intent_id=pid,
                bag_snapshot=bag_snapshot,
            )

            for item_id, quantity in bag.items():
                product = Product.objects.get(pk=item_id)
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                )

            if order.grand_total != grand_total:
                raise ValueError(
                    f"Grand total mismatch: order={order.grand_total} "
                    f"stripe={grand_total}"
                )

        except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
                content=f"Webhook error: {e}",
                status=500,
            )

        self._send_confirmation_email(order)

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
