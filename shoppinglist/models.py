from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.name}"

class Item_User(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.item.name}"
