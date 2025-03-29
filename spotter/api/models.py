import json
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    pickup_name = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    dropoff_name = models.CharField(max_length=100)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    route_instructions = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=8,
    )
    cycle_used = models.CharField(max_length=50)
    total_driving_time = models.FloatField(blank=True, default=0)
    createdOn = models.DateTimeField()

    def __str__(self):
        return json.dumps(self)

class DailyLog(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    memo = models.CharField(max_length=255)
    driving_time = models.FloatField()
    rest_breaks = ArrayField(models.FloatField())
    createdOn = models.DateTimeField()

    def __str__(self):
        return json.dumps(self)