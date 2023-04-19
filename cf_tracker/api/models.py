from django.db import models

class Car(models.Model):
        car_type = models.CharField(max_length=50)
        co2 = models.FloatField()

class Flight(models.Model):
        flight_type = models.CharField(max_length=50)
        co2 = models.FloatField()

class MotorBike(models.Model):
        bike_type = models.CharField(max_length=50)
        co2 = models.FloatField()

class PublicTransit(models.Model):
        public_transit_type = models.CharField(max_length=50)
        co2 = models.FloatField()

class Food(models.Model):
        entity = models.CharField(max_length=50)
        code = models.CharField(max_length=50, null=True, blank=True)
        year = models.CharField(max_length=50)
        co2_equivalent_per_kg = models.FloatField()