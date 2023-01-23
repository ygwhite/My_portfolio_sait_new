from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from store.models import Clothes, UserClotheRelation
from store.serializers import ClothesSerializers, UserClotheRelationSerializers


class ClothesView(ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['price']
    search_fields = ['description', 'name']
    ordering_fields = ['name', 'price']


def auth(request):
    return render(request, 'oauth.html')

class UserClothesRelationsView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserClotheRelation.objects.all()
    serializer_class = UserClotheRelationSerializers
    lookup_field = 'clothes'

    def get_object(self):


