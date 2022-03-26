from django.urls import path, include
from views import AddToCart

urlpattern = [
    path('add/cart/', AddToCart.as_view())
]