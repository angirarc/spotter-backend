import jwt
import datetime
from django.conf import settings

def generate_token(user):
    payload = {
        'id': user.id,
        'email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token