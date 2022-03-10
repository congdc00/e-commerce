from django.db import models
from django.conf import settings
from product.models import Product
from cart.models import Cart

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shipping_address = models.CharField (max_length=255, default='')
    order_description = models.TextField (default='')
    is_completed = models.BooleanField (default=False)
