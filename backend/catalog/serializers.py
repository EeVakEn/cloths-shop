import json

from rest_framework import serializers
from .models import Category, Product, ProductVariant, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('product',)


class VariantSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(read_only=True, slug_field='name')
    size = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = ProductVariant
        exclude = ('product',)


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'get_full_url')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['children'] = CategorySerializer(many=True, required=False)
        return fields


class BreadcrumbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'get_full_url')
