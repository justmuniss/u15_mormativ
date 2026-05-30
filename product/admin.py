from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from product.models import Product, Category,Book,CustomUser

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(CustomUser, UserAdmin)
