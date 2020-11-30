from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.urls import reverse

from .filters import ProductFilter, CategoryFilter
from .models import Product, Category


def all_products(request):
    products_list = Product.objects.all()
    categories_list = Category.objects.all()
    brands_column = products_list.values_list('brand_name', flat=True).distinct()

    products_filter = ProductFilter(request.GET, queryset=products_list)
    category_filter = CategoryFilter(request.GET, queryset=categories_list)

    lower_price = 0
    upper_price = 0

    if request.GET:

        if is_valid('search', request):
            search = request.GET['search']
            queries = (Q(product_name__icontains=search) | Q(product_description__icontains=search) | Q(
                brand_name__icontains=search))
            if search == "":
                messages.error(request, ("You most enter a value"))
                return redirect(reverse('products'))
            else:
                products_filter = products_filter.qs.filter(queries)
                print(products_filter)



        if is_valid('skip-value-lower', request):
            clicked = 'price'
            lower_price = float(request.GET['skip-value-lower'])
            upper_price = float(request.GET['skip-value-upper'])

    print(products_filter)

    context = {
        'products': products_filter,

        'categories': category_filter,

        'brands': brands_column,

        'lower_price': lower_price,
        'upper_price': upper_price,

    }
    return render(request, 'products/products.html', context)


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
