from django.urls import path
from .views import register, userLogin, customerList, customerFormAPI

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', userLogin, name='login'),
    path('customers/', customerList, name='customerList'),
    path('create', customerFormAPI.as_view(), name='CustoemrFORm')
]