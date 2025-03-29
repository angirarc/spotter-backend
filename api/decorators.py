import jwt
from functools import wraps
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .models import User

def protected(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        token = None
        
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        
        if not token:
            return Response({'error': 'Authentication token is missing'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['id']
            
            user = User.objects.get(id=user_id)
            request.user = user
            
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except (jwt.InvalidTokenError, User.DoesNotExist):
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
            
        return f(request, *args, **kwargs)
    
    return decorated