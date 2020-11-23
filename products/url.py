from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_products, name='products'),
    path('update/<str:brand_name>/', views.update_page, name='update_page'),
]
