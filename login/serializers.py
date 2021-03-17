from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
