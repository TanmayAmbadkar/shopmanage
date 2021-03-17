from shoppinglist.views import *
from django.urls import path

urlpatterns = [
        path('items', ItemsView.as_view(), name='items'),
        path('buy', UserItemsView.as_view(), name='buy'),
    ]
