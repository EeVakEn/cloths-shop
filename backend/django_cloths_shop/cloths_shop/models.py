from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Category_child:
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    child_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Color(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    article = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField()
    price = models.FloatField()
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.article

