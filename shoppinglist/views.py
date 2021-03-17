from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response
from login.auth import token_expire_handler, expires_in, is_token_expired
from shoppinglist.serializers import *
# Create your views here.

class ItemsView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):

        queryset = Item.objects.all()
        item_serializer = ItemSerializer(queryset, many=True)
        return Response(item_serializer.data, status=HTTP_200_OK)

class UserItemsView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):

        user = request.user
        queryset = Item_User.objects.filter(user=user)
        item_user_serializer = UserItemSerializer(queryset, many=True)
        return Response(item_user_serializer.data, status=HTTP_200_OK)

    def post(self, request):

        user = request.user
        item_id = int(request.data['id'])
        quantity = int(request.data['quantity'])
        try:
            item = Item.objects.get(id=item_id)

        except Item.DoesNotExist:
            return Response({"details": "Item Invalid"} , status=HTTP_400_BAD_REQUEST)

        item.quantity-=quantity
        if item.quantity<0:
            return Response({"details": "Quantity Invalid"} , status=HTTP_400_BAD_REQUEST)


        user_item,_ = Item_User.objects.get_or_create(item=item, user=user)
        if user_item.quantity is None:
            user_item.quantity = 0
        
        user_item.quantity+=quantity
        user_item.save()
        item.save()
        return Response({"details": "Item added"}, status=HTTP_200_OK)
