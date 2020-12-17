import json
import time
from django.http import HttpResponse, request

from checkout.models import Order, ProductOrder
from products.models import Product
from profiles.models import UserProfile


class StripeWH_Handler:
    """"Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Hadle a generic /unknow/unexpected webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Hadle payment_intent_succeeded webhook from Stripe """
        intent = event.data.object
        pid = intent.id

        bag = intent.metadata.bag

        save = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details

        shipping_details = intent.shipping

        total = round(intent.charges.data[0].amount / 100, 2)

        # Clean the data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information when save_info is checked
        profile_data = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile_data = UserProfile.objects.get(user__username=username)
            print(save)
            if save == 'true':
                profile_data.full_name_profile: billing_details.name
                profile_data.email_profile: billing_details.email
                profile_data.phone_number_profile: billing_details.phone
                profile_data.country_profile: billing_details.address.country
                profile_data.city_profile: billing_details.address.city
                profile_data.address_profile: billing_details.address.line1
                profile_data.postcode_profile: billing_details.address.postal_code
                profile_data.save()
                print(billing_details)
                print(f"New name {profile_data.full_name_profile}")
                print(f"Phone {profile_data.phone_number_profile}")
                print(f"User {profile_data.user}")
        tried = 1
        order_exists = False
        order = None
        while tried <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    city__iexact=shipping_details.address.city,
                    address__iexact=shipping_details.address.line1,
                    postcode__iexact=shipping_details.address.postal_code,
                    total_to_pay=total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                tried += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order {order} already in database',
                status=200
            )

        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile_data,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    city=shipping_details.address.city,
                    address=shipping_details.address.line1,
                    postcode=shipping_details.address.postal_code,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = ProductOrder(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} error: {e}',
                    status=500
                )

        print(order.full_name)
        print(order.email)
        print(order.phone_number)
        print(order.country)
        print(order.city)
        print(order.address)
        print(order.postcode)
        print(order.original_bag)


        return HttpResponse(
            content=f'Webhook received: {event["type"]} success: Created order {order} in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Hadle payment_intent_failed webhook from Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
