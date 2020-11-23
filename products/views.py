from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from .models import Product
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
    brands = Product.objects.all().values_list('brand_name', flat=True).distinct()
    brands_filtered = None
    # if request.GET:
    #     if is_valid('search', request):
    #         search = request.GET['search']
    #         products = products.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search))

    # current_brands = brands.filter(brand_name__in=checked_brand)

    if request.GET:
        if is_valid('brand_name', request):
            brand_name = request.GET['brand_name']
            products = products.filter(brand_name__icontains=brand_name)
            brands_filtered = brands.filter(brand_name__icontains=brand_name)

    context = {
        'brands': brands,
        'products': products,
        'brands_filtered': brands_filtered,
    }

    return render(request, 'products/products.html', context)


def update_page(request):
    products = Product.objects.all()
    brands = Product.objects.all().values_list('brand_name', flat=True).distinct()
    brands_filtered = None
    if request.GET:
        if is_valid('brand_name', request):
            brand_name = request.GET['brand_name']
            products = products.filter(brand_name__icontains=brand_name)
            brands_filtered = brands.filter(brand_name__icontains=brand_name)

    template = 'products/products.html'
    context = {
        'brands': brands,
        'products': products,
        'brands_filtered': brands_filtered,
    }
    return render(request, template, context)