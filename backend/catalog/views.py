from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


@api_view(['GET'])
def showmultiplemodels(request):
    ProdObj = Product.objects.all()
    VarObj = ProductVariant.objects.all()
    ProdSerializeObj = ProductDetailSerializer(ProdObj, many=True)
    VarSetializeObj = ProductVariantSerializer(VarObj, many=True)
    ResModel = ProdSerializeObj.data + VarSetializeObj.data
    return Response(ResModel)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.filter(is_available=True)
