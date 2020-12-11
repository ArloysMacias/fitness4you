import json
from decimal import Decimal

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from .forms import OrderForm
from bag.contexts import bag_content
import stripe
from django.conf import settings

from .models import Order


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'country': request.POST.get('country'),
            'city': request.POST.get('city'),
            'address': request.POST.get('address'),
            'postcode': request.POST.get('postcode'),
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            order_form.save()
            # order = order_form.save()
            try:
                for item_id, quantity in bag.items():
                    product = get_object_or_404(Product, pk=item_id)
                    bag_items.append({
                        'order': order,
                        'id': item_id,
                        'quantity': quantity,
                        'product': product,
                    })
            except Product.DoesNotExist:
                messages.error(request, "Sorry : Some product that you bought does not exist in our database")
                order.delete()
                return redirect(reverse('shopping_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "Sorry : Your order is not valid, please check again your information")
    else:
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

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    template = 'checkout/checkout.html'
    return render(request, template, context)


def checkout_success(request, order_number):
    """A view to show the successful user payment"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request,
                     f'Successful order: Your order {order_number} will be processed. A confirmation email will be '
                     f'sent to {order.email}')
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
