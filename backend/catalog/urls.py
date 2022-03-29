from django.urls import path
from .views import ProductDetailView, ProductInfoListView, CategoryView, ProductCategoryListView
app_name = "catalog"

urlpatterns = [
    path('products/<str:article_slug>/', ProductDetailView.as_view()),
    path('products/', ProductInfoListView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('<int:cat_id>/', ProductCategoryListView.as_view())
]