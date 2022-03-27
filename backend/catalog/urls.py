from django.urls import path
from .views import ProductDetailView, ProductInfoListView, CategoryView
app_name = "catalog"

urlpatterns = [
    path('products/<str:article_slug>/', ProductDetailView.as_view()),
    path('products/', ProductInfoListView.as_view()),
    path('categories/', CategoryView.as_view()),
]
