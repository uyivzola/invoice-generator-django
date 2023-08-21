from django.contrib import admin

from .models import Seller, Buyer, Product


admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Product)
