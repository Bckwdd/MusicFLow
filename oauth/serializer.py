from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
    """
    Сериалізація даних від Гугл
    """
    email = serializers.EmailField()
    token = serializers.CharField()
