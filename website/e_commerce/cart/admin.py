from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'item', 'quantity']

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
