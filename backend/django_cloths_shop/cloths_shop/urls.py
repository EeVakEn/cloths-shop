from django.urls import path, include
from .views import *

app_name = "cloths_shop"

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/', ProductsListView.as_view())
]
