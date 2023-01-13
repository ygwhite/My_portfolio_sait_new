from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from store.models import Clothes
from store.serializers import ClothesSerializers


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
