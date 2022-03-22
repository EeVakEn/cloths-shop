import mptt
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import RegexValidator


# mptt for requrcieve tree

class Category(MPTTModel):
    name = models.CharField(max_length=255, verbose_name='Название категррии')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родительская категория')
    slug = models.SlugField(verbose_name='Слаг категории (отображается в URL)', unique=True)

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent'

    def __str__(self):
        return self.get_level() * ' ' + self.name


mptt.register(Category, order_insertation_by=['name'])


class Color(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]{6,6}$', '6 символов. Цифры или буквы латинского алфавита.')


class Product(models.Model):
    article = models.CharField(max_length=6, verbose_name='Артикул', db_index=True, unique=True, primary_key=True, validators=[alphanumeric])
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Картинка', upload_to='img/products/')
    price = models.FloatField(verbose_name='Цена')
    color = models.ManyToManyField(Color, verbose_name='Цвет')
    size = models.ManyToManyField(Size, verbose_name='Размер')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} {}'.format(self.article, self.name)

# class ProductColorSize(models.Model):
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
#     color_id = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет')
#     size_id = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
#     quantity = models.PositiveIntegerField(verbose_name='Количество товаров с таким цветом и размером')
#
#     class Meta:
#         unique_together = ('product_id', 'color_id', 'size_id')
#
#     def __str__(self):
#         return '{}-{}-{}'.format(self.product_id.article, self.color_id.name, self.size_id.name)
