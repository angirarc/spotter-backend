import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password

from .utils import generate_token
from .decorators import protected
from .models import User, Trip, DailyLog
from .serializers import UserSerializer, TripSerializer, LogSerializer

@api_view(['GET'])
@protected
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
@protected
def user_details(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif (request.method == 'PATCH'):
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_user(request):
    data = request.data

    if User.objects.filter(email=data['email']).exists():
        return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
    
    if 'password' in data:
        data['password'] = make_password(data['password'])

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        token = generate_token(user)
        return Response({
            'user': serializer.data,
            'token': token
        }, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not check_password(password, user.password):
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token = generate_token(user)
    
    serializer = UserSerializer(user)
    return Response({
        'user': serializer.data,
        'token': token
    })

@api_view(['GET', 'POST'])
@protected
def trip_operations(request):
    if (request.method == 'GET'):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        data['user'] = request.user.id
        data['createdOn'] = datetime.now()

        serializer = TripSerializer(data=data)
        if serializer.is_valid():
            trip = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
@protected
def trip_details(request, id):
    try:
        trip = Trip.objects.get(id=id)
    except Trip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    elif (request.method == 'PATCH'):
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@protected
def trip_log_details(request, id):
    try:
        trip = Trip.objects.get(id=id)
    except Trip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        logs = DailyLog.objects.all(trip=id)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        data['trip'] = trip.id
        data['createdOn'] = datetime.now()

        serializer = LogSerializer(log, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE'])
@protected
def log_details(request, id):
    try:
        log = DailyLog.objects.get(id=id)
    except DailyLog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'PATCH'):
        serializer = LogSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)