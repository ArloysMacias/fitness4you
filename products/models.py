from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    average_flavor_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    brand_name = models.CharField(max_length=254, blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True)
    number_of_flavors = models.IntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(100)], null=True, blank=True)
    number_of_reviews = models.IntegerField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(9999)], null=True, blank=True)
    overall_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_serving = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_category = models.CharField(max_length=254, null=True, blank=True)
    product_description = models.TextField()
    product_name = models.CharField(max_length=254)
    top_flavor_rated = models.CharField(max_length=254, null=True, blank=True)
    verified_buyer_number = models.IntegerField(validators=[MinValueValidator(0),
                                                            MaxValueValidator(9999)], null=True, blank=True)
    verified_buyer_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name

