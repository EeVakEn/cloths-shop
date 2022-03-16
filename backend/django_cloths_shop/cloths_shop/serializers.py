from rest_framework import serializers
from models import Product, Color, Size, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ColorSerial(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"