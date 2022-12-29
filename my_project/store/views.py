from rest_framework.viewsets import ModelViewSet

from store.models import Clothes
from store.serializers import ClothesSerializers


class ClothesView(ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers


