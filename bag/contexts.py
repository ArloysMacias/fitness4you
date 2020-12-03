from decimal import Decimal

from django.shortcuts import get_object_or_404

from products.models import Product


def bag(request):
    bag_items = []
    sum_total = 0
    amount_of_products = 0

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        digits = [int(x) for x in str(quantity)]
        quantity = sum(digits)
        total_item_price = Decimal(quantity) * Decimal(product.price)
        sum_total += total_item_price
        amount_of_products += int(quantity)
        bag_items.append({
            'id': item_id,
            'quantity': quantity,
            'product': product,
            'total_item_price': total_item_price,
        })

    context = {
        'bag_items': bag_items,
        'sum_total': sum_total,
        'amount_of_products': amount_of_products,
    }
    return context
