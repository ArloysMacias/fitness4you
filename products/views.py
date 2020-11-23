from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from .models import Product
from django.contrib import messages
from django.db.models import Q
from .filters import ProductFilter


def is_valid(form_parameter, request):
    if form_parameter in request.GET and form_parameter != '' and form_parameter is not None:
        return True
    else:
        messages.error(request, f"The criteria {form_parameter} is not valid")
        return redirect('products')


# Create your views here.
def all_products(request):
    """A view to show all products"""

    products = Product.objects.all()
    brands = Product.objects.all().values_list('brand_name', flat=True).distinct()
    current_brands = None
    # if request.GET:
    #     if is_valid('search', request):
    #         search = request.GET['search']
    #         products = products.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search))

    # current_brands = brands.filter(brand_name__in=checked_brand)

    # if request.method == "POST":
    #     if request.POST.get('txtvalues'):
    #         checked_brand = request.GET['txtvalues'].split[',']
    #         current_brands = brands.filter(brand_name__icontains=checked_brand)
    #         products = products.filter(brand_name__icontains=checked_brand)

    if request.GET:

        if is_valid('brand_name', request):
                # brands = request.POST('brand_name')
                # checked_brand = request.POST.get('txtvalues', False)
                # brands = request.POST.get('brand_name')
                brand_name = request.GET['brand_name']
                products = products.filter(brand_name__icontains=brand_name)

    context = {
        'brands': brands,
        'products': products,
    }

    return render(request, 'products/products.html', context)


def save_values(request):
    if request.method == "POST":
        if request.POST.get('brand_name'):
            savedata = Product()
            savedata.brand_name = request.GET['brand_name']
            savedata.save()
            return render(request, 'products/products.html')
    else:
        return render(request, 'products/products.html')
