from django.urls import path
from .views import CustomerAPIList

urlpatterns = [
    path('customers/', CustomerAPIList.as_view(), name='customers-list'),
]