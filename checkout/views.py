from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('shopping_bag'))
        messages.error(request, "There is nothing in the bag at the moment")

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hoo1UD7nSCOWtUZkEuKcN1DQsKWA0YLNoAtjpVeThd4nlPfmESBpCJiO3lHptm4gZTELoi62F6PFoWeA1O8vnwc00gHDT27AK',
        'client_secret': 'test client secret'
    }
    return render(request, template, context)
