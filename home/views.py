from django.shortcuts import render
from products.models import Product


# Create your views here.

def index(request):
    """A view to return the index page"""
    products_list = Product.objects.all()
    popular_products = sorted(products_list, key=lambda x: x.overall_rating, reverse=True)[:3]
    print(popular_products)
    context = {
        'products': popular_products,
    }
    return render(request, 'home/index.html', context)
