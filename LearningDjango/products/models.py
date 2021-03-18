from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.TextField(default='default text here')
    description = models.TextField(default='default text here')
    price = models.TextField(default='default text here')
    summary = models.TextField(default='default text here')
