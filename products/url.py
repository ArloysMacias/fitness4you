from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:id>/', views.add_to_shopping_bag, name='add_to_shopping_bag'),
]
