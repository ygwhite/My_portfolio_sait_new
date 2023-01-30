import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase

from store.models import Clothes, UserClotheRelation
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
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('clothes-list')
        response = self.client.get(url, data={'search': 'Футболка'})
        serializer_data = ClothesSerializers([self.clothes_1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Clothes.objects.all().count())
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
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(4, Clothes.objects.all().count())

    def test_update(self):
        url = reverse('clothes-detail', args=(self.clothes_1.id,))
        data = {
            "name": self.clothes_1.name,
            "description": "Тест на апдейт",
            "quantity": 55,
            "price": 12397
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.clothes_1.refresh_from_db()
        self.assertEqual(12397, self.clothes_1.price)
        self.assertEqual("Тест1", self.clothes_1.description)

    def test_delete(self):
        url = reverse('clothes-detail', args=(self.clothes_3.id,))
        url2 = reverse('clothes-list')
        self.client.force_login(self.user)
        response = self.client.delete(url)
        delete_data = self.client.get(url2, data={'search': 'Свитер'})
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code, response.data)
        self.clothes_1.refresh_from_db()
        self.assertEqual([], delete_data.data)

class ClothesApiTestRelation(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='user_test1')
        self.user2 = User.objects.create(username='user_test2')
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

    def test_like_favorites_rate(self):
        url = reverse('userclotherelation-detail', args=(self.clothes_2.id, ))
        data = {
            "like": True,
            "in_favorites": True,
            "rate": 4,

        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        relation = UserClotheRelation.objects.get(user=self.user, clothes=self.clothes_2)
        self.assertTrue(relation.like)
        self.assertTrue(relation.in_favorites)
        self.assertEqual(4, relation.rate)
