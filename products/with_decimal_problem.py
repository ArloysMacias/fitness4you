# from django.shortcuts import render, redirect
# from .models import Product, Category
# from django.contrib import messages
# from django.db.models import Q
#
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
# def updated_filter(parameter, request):
#     if request.GET:
#         if request.session[parameter]:
#             result = request.session[parameter]
#         else:
#             result = request.GET[parameter]
#     return result
#
#
# def all_products(request):
#     """A view to show all products"""
#
#     products = Product.objects.all()
#     categories = Category.objects.all()
#
#     overall_rating_column = products.values_list('overall_rating', flat=True).distinct()
#     overall_rating_filtered = {}
#     overall_rating_selected = 0
#
#     brands_column = products.values_list('brand_name', flat=True).distinct()
#     brand_selected = {}
#
#     list_categories_friendly_name = categories.values_list('friendly_name', flat=True).distinct()
#     category_selected = None
#
#     price_column = products.values_list('price', flat=True)
#     lower_price = 0
#     upper_price = 0
#
#     # if request.GET:
#     #     if is_valid('search', request):
#     #         search = request.GET['search']
#     #         products = products.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search))
#     #
#     # current_brands = brands.filter(brand_name__in=checked_brand)
#
#     if request.GET:
#
#         if is_valid('overall_rating', request):
#             overall_rating_selected = float(request.GET['overall_rating'])
#             products = products.filter(overall_rating__gte=overall_rating_selected)
#             overall_rating_filtered = overall_rating_column.filter(overall_rating__gte=overall_rating_selected).first()
#
#         if is_valid('brand_name', request):
#             brand_name = request.GET['brand_name']
#             products = products.filter(brand_name__icontains=brand_name)
#             brand_selected = brands_column.filter(brand_name__icontains=brand_name).first()
#
#         if is_valid('category', request):
#             category_friendly = request.GET['category']
#             products = products.filter(category__friendly_name__exact=category_friendly)
#             category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()
#
#         if is_valid('skip-value-lower', request):
#             lower_price = float(request.GET['skip-value-lower'])
#             upper_price = float(request.GET['skip-value-upper'])
#             products = products.filter(Q(price__gte=lower_price) & Q(price__lte=upper_price))
#
#     context = {
#         'products': products,
#
#         'overall_rating_selected': overall_rating_selected,
#         'overall_rating_filtered': overall_rating_filtered,
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


from decimal import Decimal
from django.utils.formats import sanitize_separators
from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q


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


def updated_filter(parameter, request):
    result = None
    if type(parameter) == int:
        result = 0
    if type(parameter) == float:
        result = sanitize_separators(0.0)
    if type(parameter) == str:
        result = ""

    if is_valid(parameter, request):
        if request.GET:
            if request.session[parameter]:
                result = request.session[parameter]
            else:
                result = request.GET.get(parameter)
    print(result)
    return result


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

    brand_name = None
    category_friendly = None

    filter_by_rating = Q()
    filter_by_brand = Q()
    filter_by_category = Q()
    filter_by_price = Q()

    clicked = None

    # if request.GET:
    #     if is_valid('search', request):
    #         search = request.GET['search']
    #         products = products.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search))
    #
    # current_brands = brands.filter(brand_name__in=checked_brand)

    if request.GET:
        if is_valid('overall_rating', request):
            clicked = 'rating'
            overall_rating_selected = float(request.GET['overall_rating'])
            filter_by_rating = Q(overall_rating__gte=overall_rating_selected)
            request.session['filter_by_rating'] = 'Q(overall_rating__gte=overall_rating_selected)'
            request.session['overall_rating'] = 'overall_rating'

            brand_name = updated_filter('brand_name',request)
            brand_selected = brands_column.filter(brand_name__exact=brand_name).first()
            filter_by_brand = Q(brand_name__exact=brand_name)
            request.session['filter_by_brand'] = 'Q(brand_name__exact=brand_name)'

            category_friendly = updated_filter('category', request)
            category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()
            filter_by_category = Q(category__friendly_name__exact=category_friendly)
            request.session['filter_by_category'] = 'Q(category__friendly_name__exact=category_friendly)'

            lower_price = Decimal(updated_filter('skip-value-lower',request))
            upper_price = Decimal(updated_filter('skip-value-upper',request))
            filter_by_price = Q(price__gte=lower_price) & Q(price__lte=upper_price)

        if is_valid('brand_name', request):
            clicked = 'brand'
            brand_name = request.GET['brand_name']
            brand_selected = brands_column.filter(brand_name__exact=brand_name).first()
            filter_by_brand = Q(brand_name__exact=brand_name)
            request.session['filter_by_brand'] = 'Q(brand_name__exact=brand_name)'
            request.session['brand_name'] = brand_selected

            overall_rating_selected = float(updated_filter('overall_rating', request))
            filter_by_rating = Q(overall_rating__gte=overall_rating_selected)
            request.session['filter_by_rating'] = 'Q(overall_rating__gte=overall_rating_selected)'

            category_friendly = updated_filter('category',request)
            category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()
            filter_by_category = Q(category__friendly_name__exact=category_friendly)
            request.session['filter_by_category'] = 'Q(category__friendly_name__exact=category_friendly)'

            lower_price = Decimal(updated_filter('skip-value-lower',request))
            upper_price = Decimal(updated_filter('skip-value-upper',request))
            filter_by_price = Q(price__gte=lower_price) & Q(price__lte=upper_price)

        if is_valid('category', request):
            clicked = 'category'
            category_friendly = request.GET['category']
            category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()
            filter_by_category = Q(category__friendly_name__exact=category_friendly)
            request.session['filter_by_category'] = 'Q(category__friendly_name__exact=category_friendly)'
            request.session['category'] = category_selected

            overall_rating_selected = sanitize_separators(updated_filter('overall_rating', request))
            filter_by_rating = Q(overall_rating__gte=overall_rating_selected)
            request.session['filter_by_rating'] = 'Q(overall_rating__gte=overall_rating_selected)'

            brand_name = updated_filter('brand_name',request)
            brand_selected = brands_column.filter(brand_name__exact=brand_name).first()
            filter_by_brand = Q(brand_name__exact=brand_name)
            request.session['filter_by_brand'] = 'Q(brand_name__exact=brand_name)'

            lower_price = Decimal(updated_filter('skip-value-lower',request))
            upper_price = Decimal(updated_filter('skip-value-upper',request))
            filter_by_price = Q(price__gte=lower_price) & Q(price__lte=upper_price)

        if is_valid('skip-value-lower', request):
            clicked = 'price'
            lower_price = Decimal(request.GET['skip-value-lower'])
            upper_price = Decimal(request.GET['skip-value-upper'])
            filter_by_price = Q(price__gte=lower_price) & Q(price__lte=upper_price)
            request.session['filter_by_price'] = 'Q(price__gte=lower_price) & Q(price__lte=upper_price)'
            request.session['skip-value-lower']=lower_price

            overall_rating_selected = float(updated_filter('overall_rating', request))
            filter_by_rating = Q(overall_rating__gte=overall_rating_selected)
            request.session['filter_by_rating'] = 'Q(overall_rating__gte=overall_rating_selected)'

            brand_name = updated_filter('brand_name', request)
            brand_selected = brands_column.filter(brand_name__exact=brand_name).first()
            filter_by_brand = Q(brand_name__exact=brand_name)
            request.session['filter_by_brand'] = 'Q(brand_name__exact=brand_name)'

            category_friendly = updated_filter('category',request)
            category_selected = list_categories_friendly_name.filter(friendly_name__exact=category_friendly).first()
            filter_by_category = Q(category__friendly_name__exact=category_friendly)
            request.session['filter_by_category'] = 'Q(category__friendly_name__exact=category_friendly)'

        products = products.filter(
            filter_by_price &
            filter_by_category &
            filter_by_brand &
            filter_by_rating
        )

        products = products.filter()

    context = {
        'products': products,
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
