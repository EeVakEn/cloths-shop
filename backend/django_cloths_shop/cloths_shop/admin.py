from django.contrib import admin
from .models import Product, Color, Size, Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)


# Register your models here.
