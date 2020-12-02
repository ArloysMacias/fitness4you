from decimal import Decimal

from django.shortcuts import get_object_or_404

from products.models import Product


def bag(request):
    bag_items = []
    total = 0
    amount_of_products = 0

    bag = request.session.get('bag', {})

    if request.POST:
        if 'amount_to_buy' in request.POST:
            quantity = request.POST.get('amount_to_buy')
        if 'the_url' in request.POST:
            redirect_url = request.POST.get('the_url')

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        digits = [int(x) for x in quantity]
        quantity = sum(digits)
        total += Decimal(quantity) * Decimal(product.price)
        amount_of_products += int(quantity)
        bag_items.append({
            'id': item_id,
            'quantity': quantity,
            'product': product,
        })
    print(bag_items)

    context = {
        'bag_items': bag_items,
        'total': total,
        'amount_of_products': amount_of_products,
    }
    return context
