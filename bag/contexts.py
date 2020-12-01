from products.models import Product


def bag(request):
    bag_items = []
    total = 0
    amount_of_products = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'amount_of_products': amount_of_products,
    }
    return context
