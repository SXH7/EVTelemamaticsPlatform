from django.urls import path
from .views import registerDevice, resttest

urlpatterns = [
    path('register/', registerDevice, name='deviceRegister'),
    path('apitest/', resttest.as_view(), name='apitest')
]