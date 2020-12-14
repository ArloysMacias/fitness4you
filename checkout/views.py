import json
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from products.models import Product
from .forms import OrderForm
from bag.contexts import bag_content
import stripe
from django.conf import settings

from .models import Order, ProductOrder
import json


@require_POST
def cache_checkout(request):
    try:
        pid = request.POST.get('client_secret').split('secret')[0]
        pid = pid[:-1]
        print(pid)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid, metadata={
                'bag': json.dumps(request.session.get('bag', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
            })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry we can not process your payment. Try later')
        return HttpResponse(content=e, status=400)


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
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = ProductOrder(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, "Sorry : Some product that you bought does not exist in our database")
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to if all is well
            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. ' 'Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There is nothing in the bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_content(request)
        total = current_bag['sum_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """A view to show the successful user payment"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request,
                     f'Successful order: Your order {order_number} will be processed. A confirmation email will be ' f'sent to {order.email}')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
    }
    return render(request, template, context)
