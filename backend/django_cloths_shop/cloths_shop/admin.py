from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(ProductColor)
admin.site.register(Size)
admin.site.register(ProductSize)
admin.site.register(Category)
admin.site.register(ProductCategory)

# Register your models here.
