from django.test import TestCase

from store.models import Clothes
from store.serializers import ClothesSerializers


class ClothesSerializerTestCase(TestCase):
    def test_serializer(self):
        clothes_1 = Clothes.objects.create(name='Рубашка тест 1', price=25, quantity=15, description='Тест1')
        clothes_2 = Clothes.objects.create(name='Кофта тест 2', price=250, quantity=150, description='Тест2')
        serializer_data = ClothesSerializers([clothes_1, clothes_2], many=True).data
        expected_data = [
            {
                'id': clothes_1.id,
                'name': 'Рубашка тест 1',
                'description': 'Тест1',
                'quantity': 15,
                'price': '25.00',
            },
            {
                'id': clothes_2.id,
                'name': 'Рубашка тест 2',
                'description': 'Тест2',
                'quantity': 150,
                'price': '250.00',
            },
        ]
        self.assertEqual(expected_data, serializer_data)