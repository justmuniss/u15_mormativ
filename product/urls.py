from django.urls import path
from .views import product_list,category_products,category_list,contact_view,book_list,book_detail,book_create,book_update,book_delete,register_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/',category_products,name='category_products'),
    path('contact/', contact_view, name='contact'),
    path('book/', book_list, name='book_list'),
    path('book/<int:book_id>/',book_detail, name='book_detail'),
    path('book/<int:book_id>/update/', book_update, name='book_update'),
    path('book/<int:book_id>/delete/', book_delete, name='book_delete'),
    path('book/create/', book_create, name='book_create'),
    path('register/', register_view, name='register'),
]
