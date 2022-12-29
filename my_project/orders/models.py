from django.contrib.auth.models import User
from django.db import models
from store.models import Clothes


class SalesOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    clothes = models.ManyToManyField(Clothes)

    def __str__(self):
        return self.name

