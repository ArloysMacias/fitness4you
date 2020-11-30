import generics
import django_filters
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category


# class UserFilter(django_filters.FilterSet):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', ]

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class ProductFilter(django_filters.FilterSet):
    categories = NumberInFilter(field_name='category', lookup_expr='in')

    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    overall_rating = django_filters.NumberFilter(field_name='overall_rating', lookup_expr='gt')
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = Product
        fields = {
            'brand_name': ['exact', ],
            'category': ['exact'],
        }

    def search_filter(self, queryset, name, value):
        if value == "":
            messages.error(request, "You most enter a value")
            return redirect(reverse('products'))
        else:
            return Product.objects.filter(
                Q(product_name__icontains=value) | Q(product_description__icontains=value) | Q(
                    brand_name__icontains=value)
            )

class CategoryFilter(django_filters.FilterSet):
    friendly_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category

        fields = {
            'friendly_name': ['exact', ],
            'name': ['exact', ],
        }
