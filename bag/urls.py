from . import views
from django.urls import path

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<product_id>/', views.add_to_bag, name='add_to_bag'),
    path('update_bag_amount/', views.update_bag_amount, name='update_bag_amount'),
]
