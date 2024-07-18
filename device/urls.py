from django.urls import path
from .views import DeviceForm

urlpatterns = [
    path('register/', DeviceForm, name='deviceRegister'),
]