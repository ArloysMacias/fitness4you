from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from bag.contexts import bag_content
import stripe
from django.conf import settings


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('shopping_bag'))
        messages.error(request, "There is nothing in the bag at the moment")

    current_bag = bag_content(request)
    total_to_pay_from_bag = current_bag['sum_total']
    stripe_total_to_pay = round(total_to_pay_from_bag)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total_to_pay,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    return render(request, template, context)
