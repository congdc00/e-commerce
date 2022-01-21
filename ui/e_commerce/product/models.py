from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField (default='', max_length='')
    slug = models.CharField (max_length=100, default='')
    description = models.TextField (default='')
    active = models.BooleanField (default=True)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(null = True)
    price = models.IntegerField()
    number = models.IntegerField()
    describe = models.TextField(null = True, max_length = 300)
    infomation = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.name
