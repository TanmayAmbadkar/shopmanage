from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response
from login.serializers import UserSerializer, UserSigninSerializer, UserSignUpSerializer
from login.auth import token_expire_handler, expires_in
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

class LoginView(APIView):

    permission_classes = [AllowAny, ]
    def post(self, request):

        signin_serializer = UserSigninSerializer(data = request.data)
        if not signin_serializer.is_valid():
            return Response(signin_serializer.errors, status = HTTP_400_BAD_REQUEST)


        user = authenticate(
                username = signin_serializer.data['username'],
                password = signin_serializer.data['password']
            )
        if not user:
            return Response({'detail': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user = user)

        is_expired, token = token_expire_handler(token)
        user_serialized = UserSerializer(user)

        return Response({
            'user': user_serialized.data,
            'expires_in': expires_in(token),
            'token': token.key
        }, status=HTTP_200_OK)

class LogoutView(APIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request):

        token = Token.objects.get(key = request.auth.key)
        token.delete()

        return Response({'detail': 'Token Deleted'}, status=HTTP_200_OK)

class SignUpView(APIView):

    permission_classes=[AllowAny,]
    def post(self, request):

        signup_serializer = UserSignUpSerializer(data = request.data)
        if not signup_serializer.is_valid():
            return Response(signup_serializer.errors, status = HTTP_400_BAD_REQUEST)

        user = authenticate(
                username = signup_serializer.data['username'],
                password = signup_serializer.data['password']
            )

        print(signup_serializer.data)
        if not user:

            user = User.objects.create_user(username = signup_serializer.data['username'],
                                       password = signup_serializer.data['password'],
                                       first_name = signup_serializer.data['first_name'],
                                       last_name = signup_serializer.data['last_name'],
                                       email = signup_serializer.data['email'],
                                       )

            token, _ = Token.objects.get_or_create(user = user)
            user_serialized = UserSerializer(user)

            return Response({
                'user': user_serialized.data,
                'expires_in': expires_in(token),
                'token': token.key
            }, status=HTTP_200_OK)

        return Response({'detail': 'Username exists'}, status=HTTP_404_NOT_FOUND)
