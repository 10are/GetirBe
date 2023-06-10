from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/')
    order = models.IntegerField()

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory_images/')
    order = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title
