from django import http
from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from django.core.cache import cache


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


def all_products(request):
    """A view to show all products"""

    products = Product.objects.all()

    categories = Category.objects.all()

    products_filtered_cache = cache
    #
    # if not products_filtered_cache:
    #     products_filtered_cache = Product.objects.all()
    #     cache.set('products_filtered_cache', products_filtered_cache)

    # products_filtered = [products.id for products in Product.objects.all()]
    # request.session['products_filtered'] = products_filtered
    # products_filtered = [Product.objects.get(id=id) for id in request.session['products_filtered']]

    overall_rating_column = products.values_list('overall_rating', flat=True).distinct()
    overall_rating_filtered = {}
    overall_rating_selected = 0

    brands_column = products.values_list('brand_name', flat=True).distinct()
    brand_selected = {}

    list_categories_friendly_name = categories.values_list('friendly_name', flat=True).distinct()
    category_selected = {}

    price_column = products.values_list('price', flat=True)
    lower_price = 0
    upper_price = 0

    clicked = None

    if request.GET:

        if is_valid('search', request):
            search = request.GET['search']
            print(search)
            queries = (Q(product_name__icontains=search) | Q(product_description__icontains=search) | Q(
                brand_name__icontains=search))
            if search == "":
                messages.error(request, ("You most enter a value"))
                return redirect(reverse('products'))
            else:
                products = products.filter(queries)

        # if is_valid('overall_rating', request):
        #     clicked = 'rating'
        #     overall_rating_selected = float(request.GET['overall_rating'])
        #     request.session['overall_rating_selected'] = overall_rating_selected
        #     queryset = Q(overall_rating__gte=request.session['overall_rating_selected'])
        #     products = products.filter(queryset)
        #     # cache.set('products_filtered_cache', queryset)
        #     cache.set('key', queryset)
        #
        # if is_valid('brand_name', request):
        #     clicked = 'brand'
        #     brand_name = request.GET['brand_name']
        #     brand_selected = brands_column.filter(brand_name__exact=brand_name).first()
        #     request.session['brand_name'] = brand_name
        #     queryset = Q(brand_name__exact=request.session['brand_name'])
        #     products = products.filter(queryset)
        #     # cache.set('products_filtered_cache', queryset)
        #     cache.set('key', queryset)
        #
        # if is_valid('category', request):
        #     clicked = 'category'
        #     category_friendly = request.GET['category']
        #     category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()
        #     request.session['category_selected'] = category_selected
        #     queryset = Q(category__friendly_name__exact=request.session['category_selected'])
        #     products = products.filter(queryset)
        #     # cache.set('products_filtered_cache', queryset)
        #     cache.set('key', queryset)
        #
        # if is_valid('skip-value-lower', request):
        #     clicked = 'price'
        #     lower_price = float(request.GET['skip-value-lower'])
        #     upper_price = float(request.GET['skip-value-upper'])
        #     request.session['lower_price'] = lower_price
        #     request.session['upper_price'] = upper_price
        #     queryset = Q(price__gte=request.session['lower_price']) & Q(price__lte=request.session['upper_price'])
        #     products = products.filter(queryset)
        #     # cache.set('products_filtered_cache', queryset)
        #     cache.set('key', queryset)

    context = {
        'products': get_queryset(request),
        "clicked": clicked,

        'overall_rating_selected': overall_rating_selected,

        'list_categories_friendly_name': list_categories_friendly_name,
        'category_selected': category_selected,

        'brands': brands_column,
        'brand_selected': brand_selected,

        'prices': price_column,
        'lower_price': lower_price,
        'upper_price': upper_price,
    }

    return render(request, 'products/products.html', context)




# from django.core import serializers
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from .models import Product, Category
# from django.contrib import messages
# from django.db.models import Q
# from django.core.cache import cache
#
# def is_valid(form_parameter, request):
#     if request.GET:
#         if form_parameter in request.GET and form_parameter != '' and form_parameter is not None:
#             return True
#     elif request.POST:
#         if form_parameter in request.POST and form_parameter != '' and form_parameter is not None:
#             return True
#     else:
#         messages.error(request, f"The criteria {form_parameter} is not valid")
#         return redirect('products')
#
#
# def all_products(request):
#     """A view to show all products"""
#
#     products = Product.objects.all()
#
#     categories = Category.objects.all()
#
#     products_filtered_cache = cache
#     #
#     # if not products_filtered_cache:
#     #     products_filtered_cache = Product.objects.all()
#     #     cache.set('products_filtered_cache', products_filtered_cache)
#
#     # products_filtered = [products.id for products in Product.objects.all()]
#     # request.session['products_filtered'] = products_filtered
#     # products_filtered = [Product.objects.get(id=id) for id in request.session['products_filtered']]
#
#     overall_rating_column = products.values_list('overall_rating', flat=True).distinct()
#     overall_rating_filtered = {}
#     overall_rating_selected = 0
#
#     brands_column = products.values_list('brand_name', flat=True).distinct()
#     brand_selected = {}
#
#     list_categories_friendly_name = categories.values_list('friendly_name', flat=True).distinct()
#     category_selected = {}
#
#     price_column = products.values_list('price', flat=True)
#     lower_price = 0
#     upper_price = 0
#
#     clicked = None
#
#     if request.GET:
#
#         if is_valid('search', request):
#             search = request.GET['search']
#             print(search)
#             queries = (Q(product_name__icontains=search) | Q(product_description__icontains=search) | Q(
#                 brand_name__icontains=search))
#             if search == "":
#                 messages.error(request, ("You most enter a value"))
#                 return redirect(reverse('products'))
#             else:
#                 products = products.filter(queries)
#
#         if is_valid('overall_rating', request):
#             clicked = 'rating'
#             overall_rating_selected = float(request.GET['overall_rating'])
#             request.session['overall_rating_selected'] = overall_rating_selected
#             queryset = Q(overall_rating__gte=request.session['overall_rating_selected'])
#             #products = products.filter(cache)
#             cache.get_or_set('products_filtered_byrating', queryset, 30)
#             cache.set('key', queryset)
#
#         if is_valid('brand_name', request):
#             clicked = 'brand'
#             brand_name = request.GET['brand_name']
#             brand_selected = brands_column.filter(brand_name__exact=brand_name).first()
#             request.session['brand_name'] = brand_name
#             queryset = Q(brand_name__exact=request.session['brand_name'])
#             #products = products.filter(queryset)
#             cache.get_or_set('products_filtered_bybrand', queryset, 30)
#
#         if is_valid('category', request):
#             clicked = 'category'
#             category_friendly = request.GET['category']
#             category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()
#             request.session['category_selected'] = category_selected
#             queryset = Q(category__friendly_name__exact=request.session['category_selected'])
#             #products = products.filter(queryset)
#             cache.get_or_set('products_filtered_bycategory', queryset, 30)
#
#         if is_valid('skip-value-lower', request):
#             clicked = 'price'
#             lower_price = float(request.GET['skip-value-lower'])
#             upper_price = float(request.GET['skip-value-upper'])
#             request.session['lower_price'] = lower_price
#             request.session['upper_price'] = upper_price
#             queryset = Q(price__gte=request.session['lower_price']) & Q(price__lte=request.session['upper_price'])
#             #products = products.filter(queryset)
#             cache.get_or_set('products_filtered_byprice', queryset, 30)
#
#         filters = cache.get_many(['products_filtered_byrating', 'products_filtered_bybrand', 'products_filtered_bycategory', 'products_filtered_byprice'])
#         for option in filters:
#             if filters[option] is None:
#                 del(filters[option])
#
#         print(filters)
#         products.filter(filters)
#
#     context = {
#         'products': products,
#         "clicked": clicked,
#
#         'overall_rating_selected': overall_rating_selected,
#
#         'list_categories_friendly_name': list_categories_friendly_name,
#         'category_selected': category_selected,
#
#         'brands': brands_column,
#         'brand_selected': brand_selected,
#
#         'prices': price_column,
#         'lower_price': lower_price,
#         'upper_price': upper_price,
#     }
#
#     return render(request, 'products/products.html', context)
