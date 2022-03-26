from django.urls import path
from . import views
from .views import ProductDetailView, ProductsListView

app_name = "catalog"

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/', ProductsListView.as_view()),
    path('multiple/', views.showmultiplemodels),
]
