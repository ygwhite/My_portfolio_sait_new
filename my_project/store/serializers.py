from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Clothes, UserClotheRelation


class ClothesSerializers(ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Clothes
        fields = ('id', 'name', 'price', 'quantity', 'like_count')

    def get_like_count(self, instance):
        return UserClotheRelation.objects.filter(clothes=instance, like=True).count()


class UserClotheRelationSerializers(ModelSerializer):
    class Meta:
        model = UserClotheRelation
        fields = ('clothes', 'like', 'in_favorites', 'rate')
