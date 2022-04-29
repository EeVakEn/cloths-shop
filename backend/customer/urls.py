from django.urls import path
from .views import CustomerAPIList, ActivateUser

urlpatterns = [
    path('customers/', CustomerAPIList.as_view(), name='customers-list'),
    path('account/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
]