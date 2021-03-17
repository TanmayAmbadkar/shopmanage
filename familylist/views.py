from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response
from login.auth import token_expire_handler, expires_in, is_token_expired
from familylist.serializers import *
from familylist.models import *
# Create your views here.

class FamilyView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):

        user = request.user
        family = None
        try:
            family = Family.objects.get(member=user)

        except Family.DoesNotExist:
            family = None

        if family is None:
            try:
                family = Family.objects.filter(head = user).first()

            except Family.DoesNotExist:
                return Response({"details": "Family does not exist"} , status=HTTP_400_BAD_REQUEST)

        head = family.head
        queryset = Family.objects.filter(head=head)
        family_serializer = FamilySerializer(queryset, many=True)

        return Response(family_serializer.data, status=HTTP_200_OK)

    def post(self, request):

        head = request.user
        username = request.data['username']
        password = request.data['password']
        user = authenticate(
                username = username,
                password = password,
            )

        if not user:
            return Response({'detail': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

        try:
            family = Family.objects.get(member=user)
            return Response({"details": "Already part of some family"}, status=HTTP_400_BAD_REQUEST)
        except Family.DoesNotExist:
            family = None

        if family is None:
            try:
                family = Family.objects.get(head = user)
                return Response({"details": "Cannot add to family"}, status=HTTP_400_BAD_REQUEST)
            except Family.DoesNotExist:
                family = None


        family = Family(head=head, member=user)
        family.save()

        return Response({"details": "Member added to Family"}, status=HTTP_200_OK)


class FamilyItemsView(APIView):

    permission_classes = [IsAuthenticated, ]

    def get(self, request):

        user = request.user
        family = None
        try:
            family = Family.objects.get(member=user)

        except Family.DoesNotExist:
            family = None

        if family is None:
            try:
                family = Family.objects.filter(head = user).first()

            except Family.DoesNotExist:
                return Response({"details": "Family does not exist"} , status=HTTP_400_BAD_REQUEST)

        queryset = Item_Family.objects.filter(family=family)
        family_serializer = FamilyItemSerializer(queryset, many=True)

        return Response(family_serializer.data, status=HTTP_200_OK)


    def post(self, request):

        user = request.user
        family = None
        try:
            family = Family.objects.get(member=user)

        except Family.DoesNotExist:
            family = None

        if family is None:
            try:
                family = Family.objects.filter(head = user).first()

            except Family.DoesNotExist:
                return Response({"details": "Family does not exist"} , status=HTTP_400_BAD_REQUEST)

        item_id = int(request.data['id'])
        quantity = int(request.data['quantity'])
        try:
            item = Item.objects.get(id=item_id)

        except Item.DoesNotExist:
            return Response({"details": "Item Invalid"} , status=HTTP_400_BAD_REQUEST)

        item.quantity-=quantity
        if item.quantity<0:
            return Response({"details": "Quantity Invalid"} , status=HTTP_400_BAD_REQUEST)


        user_item,_ = Item_Family.objects.get_or_create(item=item, family=family)
        if user_item.quantity is None:
            user_item.quantity = 0
        user_item.quantity+=quantity
        user_item.save()
        item.save()

        return Response({"details": "Item added"}, status=HTTP_200_OK)
