from django.urls import path
from .views import register, userLogin

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', userLogin, name='login'),
]