import datetime
import jwt
from django.conf import settings


from datetime import timedelta


def create_token(user_id: int) -> dict:
    """
    Створення токена
    """
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        'user_id': user_id,
        'access_token': create_access_token(
            data={'user_id': user_id}, expires_delta=access_token_expires
        ),
        'token_type': 'Token',
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Створення access token
    """
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire, 'sub': 'access'})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

