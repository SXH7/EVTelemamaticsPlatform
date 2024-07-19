from django.urls import path
from .views import registerDevice

urlpatterns = [
    path('register/', registerDevice, name='deviceRegister'),
]