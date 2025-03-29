from django.urls import path
from .views import create_user, login, me, get_users, user_details, trip_operations, trip_details, end_trip, trip_log_details, log_details

urlpatterns = [
    # Auth routes
    path('signup/', create_user, name='create_user'),
    path('login/', login, name='login'),
    # User routes
    path('me/', me, name='me'),
    path('users/', get_users, name='get_users'),
    path('users/<int:id>', user_details, name='user_details'),
    # Trip routes
    path('trips/', trip_operations, name='trip_operations'),
    path('trips/<int:id>', trip_details, name='trip_details'),
    path('trips/<int:id>/logs', trip_log_details, name='trip_log_details'),
    path('trips/<int:id>/end', end_trip, name='end_trip'),
    # Log routes
    path('logs/<int:id>', log_details, name='log_details'),
]