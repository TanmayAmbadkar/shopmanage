from rest_framework import serializers
from shoppinglist.models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_User
        fields = '__all__'
