# core/models.py
from django.db import models

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, default="available")
