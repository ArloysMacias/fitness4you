from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from products.models import Product


def shopping_bag(request):
    """A view to see the lis of products that the user has added to the cart"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, id):
    """A view to add product and quantity to the cart"""
    if request.POST:
        if 'amount_to_buy' in request.POST:
            quantity = request.POST.get('amount_to_buy')
        else:
            quantity = 1

        if 'the_url' in request.POST:
            redirect_url = request.POST.get('the_url')
        else:
            redirect_url = 'products/products.html'

    bag = request.session.get('bag', {})

    if id in list(bag.keys()):
        bag[id] += quantity
    else:
        bag[id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
