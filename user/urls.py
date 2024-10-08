from django.urls import path
from .views import register, userLogin, customerList, customerFormAPIView, cuserFormAPIView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', userLogin, name='login'),
    path('customers/', customerList, name='customerList'),
    path('customers/create', customerFormAPIView, name='customerForm'),
    path('customers/user/create', cuserFormAPIView, name='cuserForm'),
]