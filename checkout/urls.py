from . import views
from django.urls import path
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout/', views.cache_checkout, name='cache_checkout'),
    path('wh/', webhook, name='webhook'),
]
