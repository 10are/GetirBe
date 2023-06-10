from django.db import models
from ckeditor.fields import RichTextField
from category.models import *

# Create your models here.

class Attribute(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = RichTextField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title
