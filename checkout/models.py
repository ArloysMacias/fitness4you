from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from products.models import Product
import uuid
from django.utils import timezone

from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Select country *', null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    address = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    total_to_pay = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    date = models.DateTimeField(auto_now_add=False, default=timezone.now, null=False, verbose_name="Date of order")
    original_bag = models.TextField(null=False, blank=False, default='')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='orders')

    def generate_order_number(self):
        """Generate a unique id usign UUID"""
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """Overwrite the original save method and return a id (order number) in case that there isn't an order number
        yet """
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def update_price(self):
        """Suma the price of each product and return the total"""
        self.total_to_pay = self.lineitems.aggregate(Sum('product_price'))['product_price__sum'] or 0
        self.save()

    def __str__(self):
        return self.order_number


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    product_price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """Overwrite the original save method by calculating the price of each product and update the order total"""
        self.product_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order {self.order.order_number}'
