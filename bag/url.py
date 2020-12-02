from . import views
from django.urls import path


urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<product_id>/', views.add_to_bag, name='add_to_bag'),
]
