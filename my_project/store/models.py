from django.contrib.auth.models import User
from django.db import models



class Clothes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True)

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
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_favorites = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'Пользователь: {self.user.username}; Товар: (№{self.clothes.id}){self.clothes.name}; Оценка пользователя: {self.rate}'

    def save(self, *args, **kwargs):
        from store.logic import set_rating
        super().save(*args, **kwargs)
        set_rating(self.clothes)