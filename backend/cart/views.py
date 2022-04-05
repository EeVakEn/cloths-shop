from django.shortcuts import *
from django.views.decorators.http import require_POST
from rest_framework.views import APIView

from .cart import Cart
from ..catalog.models import Product

@require_POST
def cart_add(request, product_variant_id):
    cart = Cart(request)
