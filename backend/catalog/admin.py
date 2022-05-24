from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin
from nested_admin.nested import NestedStackedInline, NestedModelAdmin, NestedInlineModelAdmin

from .models import Product, Color, Size, Category, ProductVariant, Review, Order, OrderItem


class VariantInline(admin.StackedInline):
    model = ProductVariant
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'get_img', 'name', 'category',
                    'price', 'is_available', 'created_at')
    search_fields = ('article', 'name')
    list_editable = ('name', 'price', 'is_available')
    list_filter = ('is_available', 'created_at', 'updated_at')
    inlines = [VariantInline]

    date_hierarchy = 'updated_at'

    def get_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="75" />')

    get_img.short_description = 'Фото'


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'id', 'slug', 'parent')
    list_editable = ('slug', 'parent')
    prepopulated_fields = {"slug": ("name",)}  # эта штука генерит слаг
    mptt_level_ident = 20  # эта штука рисует табы
    mpt_indent_field = 'name'  # эта штука задает поле где рисовать табы


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'review_author', 'product', 'review', 'raiting', 'created_at')
    list_display_links = ('product', 'review_author')
    list_editable = ['review']
    list_filter = ('created_at', 'updated_at', 'product', 'review_author')
    search_fields = ['product__article', 'review_author__username']
    date_hierarchy = 'updated_at'


class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = (
        'get_image', 'get_article', 'get_product_name', 'get_variant_size', 'get_variant_color', 'quantity',)
    exclude = ('product',)
    extra = 0

    def get_article(self, obj):
        return str(obj.product.product.article)

    get_article.short_description = 'Артикул'

    def get_product_name(self, obj):
        return mark_safe(f'<h1>{str(obj.product.product.name)}</h1>')

    get_product_name.short_description = 'Товар'

    def get_image(self, obj):
        return mark_safe(
            f'<img src="{obj.product.product.image.url}" '
            f'style="box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);" '
            f'height="100" />')

    get_image.short_description = 'Картинка'

    def get_variant_size(self, obj):
        return obj.product.size

    get_variant_size.short_description = 'Размер'

    def get_variant_color(self, obj):
        return mark_safe(f'<div><div style="width:20px;height:20px;background-color:{obj.product.color.name};'
                         f'box-shadow: 4px 4px 8px 0px rgba(34, 60, 80, 0.2);'
                         f'border-radius: 5px;"></div><span>{obj.product.color.name}</span></div>')

    get_variant_color.short_description = 'Цвет'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'track_status', 'user', 'firstname', 'lastname', 'email', 'phone', 'delivery_type', 'address', 'total_cost', 'created_at')
    list_editable = ('track_status',)
    date_hierarchy = "created_at"
    list_filter = ('created_at', 'email', 'track_status')
    search_fields = ('email', 'phone', 'firstname', 'lastname')
    inlines = (OrderItemsInline,)


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Order, OrderAdmin)
