from django.urls import path
from .views import product_list,category_products,category_list,contact_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/',category_products,name='category_products'),
    path('contact/', contact_view, name='contact'),
]
