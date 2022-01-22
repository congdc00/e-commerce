from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from product.models import Product

# Create your models here.
class CustomUser(AbstractUser):

    num_level = ((0, "Cơ bản"), (1, "Xác thực"), (2, "Vip"))
    level = models.IntegerField (choices=num_level, default=0)

    id_card = models. IntegerField (null=True)
    phone = models. IntegerField (null=True)
    age = models. IntegerField (default=0)
    sex_choice = ((0, "Nữ"), (1, "nam"), (2, "không xác định"))
    sex = models.IntegerField (choices=sex_choice, default=2)
    address = models.CharField (default='', max_length=255)



class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

