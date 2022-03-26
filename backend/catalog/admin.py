from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Color, Size, Category, ProductVariant


class VariantInline(admin.TabularInline):
    model = ProductVariant
    list_display = ['color', 'size', 'quantity', ]
    list_editable = ['color', 'size', 'quantity', ]
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'get_img', 'name', 'category',
                    'price', 'is_available', 'created_at')
    search_fields = ('article', 'name')
    list_editable = ('name', 'price', 'is_available')
    list_filter = ('is_available', 'created_at', 'updated_at')
    inlines = [VariantInline]

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="75" />')
    get_img.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    list_editable = ('slug', 'parent')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)

# Register your models here.
