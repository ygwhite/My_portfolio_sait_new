from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
