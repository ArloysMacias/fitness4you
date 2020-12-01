from django.core.cache import cache

from products.models import Product


def bag(request):
    products = Product.objects.all()
    context = {
        'bag_items': products,
    }
    return context
