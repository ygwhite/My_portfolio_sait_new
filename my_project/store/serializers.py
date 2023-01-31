from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Clothes, UserClotheRelation


class ClothesSerializers(ModelSerializer):
    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)


    class Meta:
        model = Clothes
        fields = ('id', 'name', 'price', 'quantity', 'annotated_likes',
                  'rating')


class UserClotheRelationSerializers(ModelSerializer):
    class Meta:
        model = UserClotheRelation
        fields = ('clothes', 'like', 'in_favorites', 'rate')
