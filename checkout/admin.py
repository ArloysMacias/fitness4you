from django.contrib import admin
from .models import Order, ProductOrder


class ProductOrderAdmin(admin.TabularInline):
    model = ProductOrder
    readonly_fields = ('product_price',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductOrderAdmin,)

    readonly_fields = ('order_number', 'total_to_pay', 'stripe_pid', 'original_bag')

    fields = (
        'order_number', 'user_profile', 'full_name', 'email', 'phone_number', 'country', 'city', 'address', 'postcode',
        'total_to_pay',
        'stripe_pid', 'date', 'original_bag')

    list_display = ('order_number', 'full_name', 'email', 'phone_number', 'country', 'city', 'address', 'postcode',
                    'total_to_pay', 'date')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
