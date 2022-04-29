from functools import reduce

from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404

from .serializers import *
from .models import *
from .permissions import *


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(level=0)
        return queryset


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_available=True)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        descendants = Category.objects.get(slug=self.kwargs.get('cat_slug')).get_descendants(include_self=True)
        descendants_ids = [item.id for item in descendants]
        products = Product.objects.filter(is_available=True).filter(category__in=descendants_ids)
        return products


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        review_author = self.request.user

        serializer.save(product=product, review_author=review_author)


class ReviewListAPIView(generics.ListAPIView):
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, pk=product_id)
        return Review.objects.filter(product=product)
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]


class BreadcrumbAPIView(generics.ListAPIView):
    serializer_class = BreadcrumbSerializer

    def get_queryset(self):
        breadcrumb = Category.objects.get(slug=self.kwargs.get('cat_slug')) \
            .get_ancestors(ascending=False, include_self=True)

        return breadcrumb


class VariantDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = VariantDetailSerializer
