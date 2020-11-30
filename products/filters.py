import generics
from django import forms
import django_filters
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
    q = django_filters.CharFilter(method='my_custom_filter')

    class Meta:
        model = Product
        fields = {
            'brand_name': ['exact', ],
            'category': ['exact'],
        }
    def my_custom_filter(self, queryset, name, value):
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




# class ProductSerializer(Product):
#     pass


# class ProductsListView(generics.ListAPIView):
#     queryList = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     # filterset_class = ProductFilter
#     # filterset_fields = ('category', 'brand_name', 'category')
#
#     def get_queryset(self):
#
#         overall_rating_selected = overall_rating_selected = float(self.request.query_params.get('overall_rating', None))
#         brand_name = brand_name = self.request.query_params.get('brand_name', None)
#         category_friendly = category_friendly = self.request.query_params.get('category', None)
#         lower_price = lower_price = float(self.request.query_params.get('skip-value-lower', None))
#         upper_price = upper_price = float(self.request.query_params.get('skip-value-upper', None))
#
#         if overall_rating_selected:
#             queryList = queryList.filter(overall_rating_selected=overall_rating_selected)
#         if brand_name:
#             queryList = queryList.filter(brand_name=brand_name)
#         if category_friendly:
#             queryList = queryList.filter(category_friendly=category_friendly)
#         if lower_price:
#             queryList = queryList.filter(lower_price=lower_price)
#         if upper_price:
#             queryList = queryList.filter(upper_price=upper_price)
#
#         # results = []
#         # for choice in queryList:
#         #     results.append((choice.pk, choice.name))
#         #
#         # return http.HttpResponse(results)
#
#         return queryList
