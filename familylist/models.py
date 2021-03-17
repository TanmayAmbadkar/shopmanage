from django.db import models
from shoppinglist.models import *
from django.contrib.auth.models import User
# Create your models here.

class Family(models.Model):

    head = models.ForeignKey(User, on_delete = models.CASCADE, related_name='head')
    member = models.ForeignKey(User, on_delete = models.CASCADE, related_name='member')

    def __str__(self):
        return f"{self.head.username} {self.member.username}"

class Item_Family(models.Model):

    family = models.ForeignKey(Family, on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.family.head.username} {self.item.name}"
