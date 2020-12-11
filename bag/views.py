from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils.html import format_html

from products.models import Product


def shopping_bag(request):
    """A view to see the lis of products that the user has added to the cart"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """A view to add product and quantity to the cart"""
    product_added = Product.objects.get(pk=product_id)
    quantity = 1
    redirect_url = '/products'
    print(redirect_url)
    if request.POST:
        if 'amount_to_buy' in request.POST:
            quantity = int(request.POST.get('amount_to_buy'))
        else:
            quantity = 1

        if 'the_url' in request.POST:
            redirect_url = request.POST.get('the_url')

    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        if quantity is not None:
            if quantity is not 0:
                bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    messages.success(request, f'Added {product_added.product_name} to your bag')

    return redirect(redirect_url)


def update_bag_amount(request):
    # redirect_url = '/bag'
    if request.GET:
        # if 'the_checkout_url' in request.GET:
        #     redirect_url = request.GET['the_checkout_url']
        if 'update' in request.GET:
            list_of_parameter = request.GET['update'].split(',')
            id_product_to_update = list_of_parameter[0]
            product_to_update = Product.objects.get(pk=id_product_to_update)
            type_update = list_of_parameter[1]
            quantity = int(str(list_of_parameter[2]))
            bag = request.session.get('bag', {})
            if id_product_to_update in list(bag.keys()):
                if type_update == 'increase':
                    quantity = quantity + 1
                if type_update == 'decrease':
                    quantity = quantity - 1
                if type_update == 'remove' or quantity <= 0:
                    bag.pop(id_product_to_update)
                    message = format_html(u'{} <strong>{}</strong> {}', "Remove", product_to_update.product_name, "from the bag")
                    messages.info(request, message)
                    # messages.info(request, f'Remove product {product_to_update.product_name} from the bag')
                else:
                    bag[id_product_to_update] = quantity
                    messages.success(request, f'Updated {product_to_update.product_name} to {quantity}')

        request.session['bag'] = bag

    return redirect(reverse('shopping_bag'))
    # return redirect(redirect_url)
