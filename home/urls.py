from django.urls import path
from .views import home, raw

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('raw/', raw, name='raw'),

]