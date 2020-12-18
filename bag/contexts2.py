from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404

from products.models import Product


def bag_content(request):
    bag_items = []
    sum_total = 0
    amount_of_products = 0
    bag = request.session.get('bag', {})

    try:
        if bag == {}:
            empty_bag = {"bag_items": [], "total": 0, "count": 0}
            request.session["bag"] = empty_bag
        else:
            for item_id, quantity in bag.items():
                product = get_list_or_404(Product, pk=item_id)
                print(product)
                digits = [int(x) for x in str(quantity)]
                quantity = sum(digits)
                try:
                    total_item_price = Decimal(quantity) * Decimal(product.price)
                except Product.DoesNotExist:
                    messages.error(request, f'The product {product.product_name} dosnot have price at the moment')
                    total_item_price = Decimal(quantity) * Decimal(0)

                sum_total += total_item_price
                amount_of_products += int(quantity)
                bag_items.append({
                    'id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'total_item_price': total_item_price,
                })
    except Product.DoesNotExist:
        if request.session["bag"]:
            bag = request.session["bag"]
        else:
            bag = {"bag_items": [], "total": 0, "count": 0}
    finally:
        request.session["bag"] = bag

    context = {
        'bag_items': bag_items,
        'sum_total': sum_total,
        'amount_of_products': amount_of_products,
    }
    return context
