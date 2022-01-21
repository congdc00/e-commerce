from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField (default='', max_length=200)
    slug = models.CharField (max_length=100, default='')
    description = models.TextField (default='')
    active = models.BooleanField (default=True)

