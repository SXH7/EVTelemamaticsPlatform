from django.urls import path
from .views import home, raw, chargers, grafana_proxy

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('raw/', raw, name='raw'),
    path('assets/chargers', chargers, name='chargers'),
    path('grafana-proxy', grafana_proxy, name='proxy'),
]