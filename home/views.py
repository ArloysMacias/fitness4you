from django.shortcuts import render
from products.models import Product


# Create your views here.

def index(request):
    """A view to return the index page"""
    products_list = Product.objects.all()
    popular_products = sorted(products_list, key=lambda x: x.overall_rating, reverse=True)

    list_to_show = []
    list_popular_exclusive = []
    for product in products_list:
        if product.exclusive:
            list_popular_exclusive.append(product)

    list_to_show = list(filter(lambda product: product not in list_popular_exclusive, popular_products))
    if request.user.is_authenticated:
        list_to_show = popular_products  # ALL


    context = {
        'products': list_to_show[:3],
    }
    return render(request, 'home/index.html', context)
