from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    article = models.CharField(max_length=10)
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()


class Color(models.Model):
    name = models.CharField(max_length=30)


class ProductColor(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Size(models.Model):
    name = models.CharField(max_length=30)


class ProductSize(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=30)
    # url = models.CharField(max_length=90)


class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


