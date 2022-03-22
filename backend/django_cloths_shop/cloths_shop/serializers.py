from rest_framework import serializers
from .models import *


class ProductDetailSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    size = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = Product
        fields = '__all__'
        ordering = ['-created_at']
