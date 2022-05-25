from django.contrib import admin

# Register your models here.

from .models import CartItem,Users,Sellers,Warehouses

admin.site.register(CartItem)
admin.site.register(Users)
admin.site.register(Sellers)
admin.site.register(Warehouses)


