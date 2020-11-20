from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages
from django.db.models import Q
from .models import Category


# Create your views here.
def all_products(request):
    """A view to show all products"""

    products = Product.objects.all()
    search = None
    brand = None

    if request.GET:
        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, "Nothing is typed")
                return redirect(reverse('products'))
            queries = Q(product_name__icontains=search) | Q(product_description__icontains=search)
            products = products.filter(queries)

    if request.GET:
        if 'brand_name' in request.GET:
            brandlist = request.GET['brand_name'].split(',')
            # queries = Q(products__brand_name__in=brandlist)
            products = products.filter(brand_name__in=brandlist)

    context = {
        'products': products,
        'search': search,
        'brand': brand
    }

    return render(request, 'products/products.html', context)
