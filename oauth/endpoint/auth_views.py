from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .. import serializer
from ..services.google import check_google_auth


def google_login(request):
    """
    Сторінка входу через гугл
    """
    return render(request, 'oauth/google_login.html')


@api_view(['POST'])
def google_auth(request):
    """
    Підтвердження авторизації через Гугл
    """
    google_data = serializer.GoogleAuth(data=request.data)
    if google_data.is_valid():
        token = check_google_auth(google_data.data)
        return Response({'token': token})
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
