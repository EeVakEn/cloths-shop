from django.shortcuts import *
from rest_framework.views import APIView

from .cart import Cart
from ..cloths_shop.models import Product

class AddToCart(APIView):
    def post


def cart_add(request, product, selected_color, selected_size):
    cart = Cart(request)
    product = get_object_or_404(Product, article=cart.)
# Create your views here.
