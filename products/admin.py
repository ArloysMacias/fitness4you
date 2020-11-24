from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProducAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'product_description',
        'category',
        'price',
        'brand_name',
        'image',
        'overall_rating',
        'number_of_reviews',
        'top_flavor_rated',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProducAdmin)
admin.site.register(Category, CategoryAdmin)
