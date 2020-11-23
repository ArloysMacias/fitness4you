import django_filters
from django.forms import CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from products.models import Product

BRAND_CHOICES = (
    (0, 'MuscleTech'),
    (1, 'EVLUTION NUTRITION'),
    (2, 'BSN'),
    (3, 'Scivation'),
    (4, 'Dymatize'),
    (5, '')
)


class ProductFilter(django_filters.FilterSet):
    brand_name = django_filters.ChoiceFilter(field_name='brand_name', choices=BRAND_CHOICES, widget=CheckboxInput, default=5)

    class Meta:
        model = Product
        fields = ['brand_name']
