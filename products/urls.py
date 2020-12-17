from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
]
