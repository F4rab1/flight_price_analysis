from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings  # Import settings where MongoDB connection is stored

@api_view(['GET'])
def get_flight_prices(request):
    date = request.GET.get('date')
    city_departure = request.GET.get('city_departure')
    city_arrival = request.GET.get('city_arrival')

    if not date or not city_departure or not city_arrival:
        return Response({"error": "Missing required parameters"}, status=400)

    # Query MongoDB
    query = {
        "departure.day": date,
        "departure.city": city_departure,
        "arrival.city": city_arrival
    }
    
    flights = list(settings.FLIGHTS_COLLECTION.find(query, {"_id": 0}))  

    if not flights:
        return Response({"message": "No flights found"}, status=404)

    return Response(flights)

