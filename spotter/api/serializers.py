from rest_framework import serializers
from .models import User, Trip, DailyLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'pickup_location', 'dropoff_location', 'start_time', 'end_time', 'route_instructions', 'cycle_used', 'createdOn']
        extra_kwargs = {
            'start_time': {'read_only': True},
            'end_time': {'read_only': True},
            'createdOn': {'read_only': True}
        }

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = ['id', 'current_location', 'driving_time', 'rest_breaks', 'total_hours', 'createdOn']
        extra_kwargs = {
            'createdOn': {'read_only': True}
        }