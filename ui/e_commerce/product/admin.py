from django.contrib import admin
from product.models import Product, Category, Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'number']
    list_filter = ['price']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'active']

class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'title', 'price', 'sale_price', 'inventory', 'active']
admin.site.register(Variation, VariationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
