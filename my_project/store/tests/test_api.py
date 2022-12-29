from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Clothes
from store.serializers import ClothesSerializers


class ClothesApiTestCase(APITestCase):
    def test_get(self):
        clothes_1 = Clothes.objects.create(name='Рубашка тест 1', price=25, quantity=15, description='Тест1')
        clothes_2 = Clothes.objects.create(name='Кофта тест 2', price=250, quantity=150, description='Тест2')
        url = reverse('clothes-list')
        response = self.client.get(url)
        serializer_data = ClothesSerializers([clothes_1, clothes_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
