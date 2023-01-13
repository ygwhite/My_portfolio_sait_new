import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase

from store.models import Clothes
from store.serializers import ClothesSerializers


class ClothesApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='user_test')
        self.clothes_1 = Clothes.objects.create(name='Футболка тест 1',
                                                price=25,
                                                quantity=15,
                                                description='Тест1')
        self.clothes_2 = Clothes.objects.create(name='Кофта тест 2',
                                                price=250,
                                                quantity=150,
                                                description='Тест2')
        self.clothes_3 = Clothes.objects.create(name='Свитер тест 3',
                                                price=550,
                                                quantity=120,
                                                description='Тест3')

    def test_get(self):
        url = reverse('clothes-list')
        response = self.client.get(url)
        serializer_data = ClothesSerializers([self.clothes_1, self.clothes_2, self.clothes_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('clothes-list')
        response = self.client.get(url, data={'search': 'Футболка'})
        serializer_data = ClothesSerializers([self.clothes_1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        url = reverse('clothes-list')
        data = {
            "name": "Футболка с длинным рукавом",
            "description": "Очень тёплая",
            "quantity": 23,
            "price": 1299
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
