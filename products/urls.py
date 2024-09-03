# products/urls.py

from django.urls import path
from .views import list_products, update_product, create_product

urlpatterns = [
    path('', list_products, name='list_products'),
    path('update/<int:product_id>/', update_product, name='update_product'),
    path('create/', create_product, name='create_product'),  # New URL for creating a product

]