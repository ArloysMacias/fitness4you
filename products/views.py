from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from .filters import ProductFilter


def is_valid(form_parameter, request):
    if request.GET:
        if form_parameter in request.GET and form_parameter != '' and form_parameter is not None:
            return True
    elif request.POST:
        if form_parameter in request.POST and form_parameter != '' and form_parameter is not None:
            return True
    else:
        messages.error(request, f"The criteria {form_parameter} is not valid")
        return redirect('products')


# Create your views here.
def all_products(request):
    """A view to show all products"""

    products = Product.objects.all()
    categories = Category.objects.all()

    overall_rating_column = products.values_list('overall_rating', flat=True).distinct()
    overall_rating_filtered = {}
    overall_rating_selected = 0

    brands_column = products.values_list('brand_name', flat=True).distinct()
    brand_selected = {}

    list_categories_friendly_name = categories.values_list('friendly_name', flat=True).distinct()
    category_selected = None

    price_column = products.values_list('price', flat=True)
    lower_price = 0
    upper_price = 0

    # if request.GET:
    #     if is_valid('search', request):
    #         search = request.GET['search']
    #         products = products.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search))

    # current_brands = brands.filter(brand_name__in=checked_brand)

    if request.GET:

        if is_valid('overall_rating', request):
            overall_rating_selected = float(request.GET['overall_rating'])
            products = products.filter(overall_rating__gte=overall_rating_selected)
            overall_rating_filtered = overall_rating_column.filter(overall_rating__gte=overall_rating_selected)

        if is_valid('brand_name', request):
            brand_name = request.GET['brand_name']
            products = products.filter(brand_name__icontains=brand_name)
            brand_selected = brands_column.filter(brand_name__icontains=brand_name).first()

        if is_valid('category', request):
            category_friendly = request.GET['category']
            products = products.filter(category__friendly_name__exact=category_friendly)
            category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()

        if is_valid('skip-value-lower', request):
            if is_valid('skip-value-upper', request):
                lower_price = float(request.GET['skip-value-lower'])
                upper_price = float(request.GET['skip-value-upper'])
                products = products.filter(Q(price__gte=lower_price) & Q(price__lte=upper_price))

    context = {
        'products': products,

        'overall_rating_selected': overall_rating_selected,
        'overall_rating_filtered': overall_rating_filtered,

        'list_categories_friendly_name': list_categories_friendly_name,
        'category_selected': category_selected,

        'brands': brands_column,
        'brand_selected': brand_selected,

        'prices': price_column,
        'lower_price': lower_price,
        'upper_price': upper_price,
    }

    return render(request, 'products/products.html', context)
