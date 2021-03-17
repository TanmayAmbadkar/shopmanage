from rest_framework import serializers
from familylist.models import *

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = '__all__'

class FamilyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Family
        fields = '__all__'
