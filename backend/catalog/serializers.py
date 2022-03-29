import json

from rest_framework import serializers
from .models import Category, Product
from django.core.serializers.json import Serializer, DjangoJSONEncoder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('article', 'name', 'description', 'image', 'price', 'is_available', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'get_full_url')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['children'] = CategorySerializer(many=True, required=False)
        return fields
