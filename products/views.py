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


    context = {
        'products': products_filter,

        'categories': category_filter,

        'brands': brands_column,

    }
    return render(request, 'products/products.html', context)
