from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField (default='', max_length=200)
    slug = models.CharField (max_length=100, default='')
    description = models.TextField (default='')
    active = models.BooleanField (default=True)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    active = models.BooleanField (default=True)
    image = models.ImageField(null = True)
    price = models.IntegerField()
    number = models.IntegerField()
    describe = models.TextField(null = True, max_length = 300)
    information = models.TextField()
    rate = models.IntegerField()
    location = models.TextField()
    guide = models.TextField()
    warranty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    inventory = models. IntegerField(default=0)
    active = models.BooleanField(default=True)
