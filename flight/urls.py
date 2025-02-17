from django.urls import path
from .views import get_flight_prices

urlpatterns = [
    path('flight-prices/', get_flight_prices, name='flight-prices'),
]