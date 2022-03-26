from rest_framework import serializers
from .models import *


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        ordering = ['-created_at']

    # color = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    # size = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['color', 'size', 'quantity']
    color = serializers.SlugRelatedField(read_only=True, slug_field='name')
    size = serializers.SlugRelatedField(read_only=True, slug_field='name')

    # model_variants = ProductVariantSerializer()
    #
    # def create(self, validated_data):
    #
    #     model_variant_data = validated_data.pop('model_variants')
    #     model_product_instance = Product.objects.create(**validated_data)
    #     ProductVariant.objects.create(
    #         product=model_product_instance,
    #
    #     )

