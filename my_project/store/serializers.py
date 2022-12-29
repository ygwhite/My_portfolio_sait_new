from rest_framework.serializers import ModelSerializer

from store.models import Clothes


class ClothesSerializers(ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'
