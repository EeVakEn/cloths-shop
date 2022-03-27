import mptt
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import RegexValidator


class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название категррии')
    slug = models.SlugField(verbose_name='Слаг категории (отображается в URL)', unique=True, db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родительская категория')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent'

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.get_level() * ' ' + self.name


mptt.register(Category, order_insertation_by=['name'])


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Цвет')

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'colors'
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Size(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Размер')

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'sizes'
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Product(models.Model):
    article = models.AutoField(verbose_name='Артикул', primary_key=True)
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Картинка', upload_to='img/products/')
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Редактировано')

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return '{} {}'.format(self.article, self.name)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        db_table = 'product_variants'
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
        unique_together = ('product_id', 'color_id', 'size_id')
