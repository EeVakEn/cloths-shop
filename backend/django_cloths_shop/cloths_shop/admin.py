from django.contrib import admin
from .models import Product, Color, Size, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('article','name','description','category','image','color','price','price','size','is_available')

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)


# Register your models here.
