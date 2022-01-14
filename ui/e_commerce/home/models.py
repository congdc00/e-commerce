from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    number = models.IntegerField()
    infomation = models.TextField()
    location = models.TextField()
