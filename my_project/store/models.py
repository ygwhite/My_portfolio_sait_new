from django.contrib.auth.models import User
from django.db import models


class Clothes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class UserClotheRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ужасно!'),
        (2, 'Плохо!'),
        (3, 'Неплохо!'),
        (4, 'Отлично!'),
        (5, 'Я безумно доволен покупкой!')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothe = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_favorites = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
