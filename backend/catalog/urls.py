from django.urls import path
from .views import *
app_name = "catalog"

urlpatterns = [
    # path('products/<str:article_slug>/', ProductDetailView.as_view()),
    # path('', ProductInfoListView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('category/<str:cat_slug>/', ProductListByCategoryAPIView.as_view()),
    path('breadcrumb/<str:cat_slug>/', BreadcrumbAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('products/<int:product_id>/review/', ReviewCreateAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view())
]
