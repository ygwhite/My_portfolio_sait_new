from rest_framework.serializers import ModelSerializer

from store.models import Clothes, UserClotheRelation


class ClothesSerializers(ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'

class UserClotheRelationSerializers(ModelSerializer):
    class Meta:
        model = UserClotheRelation
        fields = ('clothes', 'like', 'in_favorites', 'rate')
