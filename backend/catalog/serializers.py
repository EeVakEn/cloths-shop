from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, authentication, status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Category, Product, ProductVariant, Review, OrderItem, Order
import locale

locale.setlocale(locale.LC_ALL, 'russian_russia')


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %B %Y, %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d %B %Y, %H:%M", read_only=True)
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
    rating = serializers.DecimalField(decimal_places=2, max_digits=3)

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


class ProductMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('article', 'name', 'description', 'image', 'price')


class VariantDetailSerializer(serializers.ModelSerializer):
    product = ProductMinimalSerializer()
    color = serializers.SlugRelatedField(read_only=True, slug_field='name')
    size = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = ProductVariant
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity",
        )


class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = VariantDetailSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity",
        )


class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemDetailSerializer(many=True)
    created_at = serializers.DateTimeField(format="%d %B %Y, %H:%M", read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "firstname",
            "lastname",
            "email",
            "phone",
            "address",
            "items"
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
