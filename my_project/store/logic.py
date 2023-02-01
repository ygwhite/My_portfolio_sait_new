from django.db.models import Avg

from store.models import UserClotheRelation


def set_rating(clothes):
    rating = UserClotheRelation.objects.filter(clothes=clothes).aggregate(rating=Avg('rate')).get('rating')
    clothes.rating = rating
    clothes.save()