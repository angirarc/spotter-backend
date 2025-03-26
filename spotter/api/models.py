from django.db import models
from django.contrib.postgres.fields import ArrayField
import json

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    route_instructions = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=8,
    )
    cycle_used = models.CharField(max_length=50)
    createdOn = models.DateField()

    def __str__(self):
        return json.dumps(self)

class DailyLog:
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()
    driving_time = models.IntegerField()
    rest_breaks = ArrayField(
        models.CharField(max_length=255, blank=True)
    )
    total_hours = models.IntegerField()
    createdOn = models.DateField()

    def __str__(self):
        return json.dumps(self)