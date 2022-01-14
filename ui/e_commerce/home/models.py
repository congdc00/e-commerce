from django.db import models
from django.conf import settings
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(null = True)
    price = models.IntegerField()
    number = models.IntegerField()
    infomation = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)