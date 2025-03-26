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
        fields = ['current_location', 'pickup_location', 'dropoff_location', 'route_instructions', 'cycle_used']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = ['start_time', 'end_time', 'driving_time', 'rest_breaks', 'total_hours']