from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'cart', 'product','shipping_address', 'order_description', 'is_completed']

admin.site.register(Order, OrderAdmin)
