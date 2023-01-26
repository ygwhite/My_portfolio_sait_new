from django.test import TestCase

from store.models import Clothes
from store.serializers import ClothesSerializers


class ClothesSerializerTestCase(TestCase):
    def test_serializer(self):
        clothes_1 = Clothes.objects.create(name='тест 3',
                                           price=25,
                                           quantity=123
                                           )
        clothes_2 = Clothes.objects.create(name='тест 5',
                                           price=13,
                                           quantity=125
                                           )
        serializer_data = ClothesSerializers([clothes_1, clothes_2], many=True).data
        expected_data = [
            {
                'id': clothes_1.id,
                'name': 'тест 3',
                'price': '25.00',
                'quantity': 123,
                'like_count': 0,

            },
            {
                'id': clothes_2.id,
                'name': 'тест 5',
                'price': '13.00',
                'quantity': 125,
                'like_count': 0

            },
        ]
        print(serializer_data)
        print('======================')
        print(expected_data)
        print('===========================================================================')
        self.assertEqual(expected_data, serializer_data)
