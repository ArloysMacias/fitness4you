from decimal import Decimal

from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404

from .filters import ProductFilter, CategoryFilter
from .models import Product, Category


def all_products(request):
    clicked = None

    products_list = Product.objects.all()
    categories_list = Category.objects.all()

    brands_column = products_list.values_list('brand_name', flat=True).distinct()

    products_filter = ProductFilter(request.GET, queryset=products_list)
    category_filter = CategoryFilter(request.GET, queryset=categories_list)

    overall_rating_selected = 0
    brand_selected = "All Brands"
    category_selected = "All Brands"
    lower_price = 0
    upper_price = 400

    sort = None
    direction = None
    current_sorting = None

    if request.GET:
        if 'overall_rating' in request.GET:
            overall_rating_selected = int(request.GET['overall_rating'])
            clicked = 'rating'
        if 'brand_name' in request.GET:
            brand_selected = (request.GET['brand_name'])
            clicked = 'brand'
        if 'category' in request.GET:
            category_selected = int(request.GET['category'])
            clicked = 'category'
        if 'price__gt' in request.GET:
            clicked = 'price'
            lower_price = Decimal(request.GET['price__gt'])
        if 'price__lt' in request.GET:
            clicked = 'price'
            upper_price = Decimal(request.GET['price__lt'])

        if 'ordering' in request.GET:
            clicked = 'filter'
            current_sorting = (request.GET['ordering'])

    context = {
        'products': products_filter,

        'categories': category_filter,

        'brands': brands_column,

        'clicked': clicked,

        'overall_rating_selected': overall_rating_selected,

        'brand_selected': brand_selected,

        'category_selected': category_selected,

        'lower_price': lower_price,
        'upper_price': upper_price,

        'current_sorting': current_sorting,

    }
    return render(request, 'products/products.html', context)


def product_details(request, id):

    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)
