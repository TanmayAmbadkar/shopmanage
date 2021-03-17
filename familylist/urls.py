from familylist.views import *
from django.urls import path

urlpatterns = [
        path('family', FamilyView.as_view(), name='family'),
        path('family/buy', FamilyItemsView.as_view(), name='famitem'),
    ]
