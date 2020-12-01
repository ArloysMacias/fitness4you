from . import views
from django.urls import path


urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
]
