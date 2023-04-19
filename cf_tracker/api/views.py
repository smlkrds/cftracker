from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Car, Flight, MotorBike, PublicTransit, Food


@api_view(['POST'])
def car_travel(request):
        distance = float(request.data['distance'])  # distance in km
        car_type_name = request.data['carType']  # car type name

        car_type = Car.objects.get(car_type=car_type_name)
        emissions_per_km = car_type.co2
        carbon_footprint = distance * emissions_per_km

        return Response({'carbon_footprint': carbon_footprint})

@api_view(['POST'])
def plane_travel(request):
        distance = float(request.data['distance'])  # distance in km
        flight_type_name = request.data['flightType']  # flight type name

        flight_type = Flight.objects.get(flight_type=flight_type_name)
        emissions_per_km = flight_type.co2
        carbon_footprint = distance * emissions_per_km

        return Response({'carbon_footprint': carbon_footprint})

@api_view(['POST'])
def motorbike_travel(request):
        distance = float(request.data['distance'])  # distance in km
        bike_type_name = request.data['bikeType']  # motorbike type name

        bike_type = MotorBike.objects.get(bike_type=bike_type_name)
        emissions_per_km = bike_type.co2
        carbon_footprint = distance * emissions_per_km

        return Response({'carbon_footprint': carbon_footprint})

@api_view(['POST'])
def public_transit_travel(request):
        distance = float(request.data['distance'])  # distance in km
        public_transit_type_name = request.data['publicTransitType']  # public transit type name

        public_transit_type = PublicTransit.objects.get(public_transit_type=public_transit_type_name)
        emissions_per_km = public_transit_type.co2
        carbon_footprint = distance * emissions_per_km

        return Response({'carbon_footprint': carbon_footprint})

@api_view(['POST'])
def food(request):
        amount = float(request.data['amount']) # amount of food that has been consumed
        food_type_name = request.data['typeOfFood']

        food_type = Food.objects.get(entity=food_type_name)
        emission_per_g = (food_type.co2_equivalent_per_kg / 1000)
        carbon_footprint = amount * emission_per_g

        return Response({'carbon_footprint': carbon_footprint})
