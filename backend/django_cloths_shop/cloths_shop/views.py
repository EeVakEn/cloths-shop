from rest_framework import generics

from .serializers import *


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
