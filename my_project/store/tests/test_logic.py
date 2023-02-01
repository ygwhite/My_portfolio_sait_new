from django.contrib.auth.models import User
from django.test import TestCase

from store.logic import set_rating
from store.models import Clothes, UserClotheRelation


class SetRatingLogicTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        self.clothes_1 = Clothes.objects.create(name='тест 3', price=25, quantity=123)

        UserClotheRelation.objects.create(user=user1, clothes=self.clothes_1, like=True, rate=5)
        UserClotheRelation.objects.create(user=user2, clothes=self.clothes_1, like=True, rate=2)
    def test_ok(self):
        set_rating(self.clothes_1)
        self.clothes_1.refresh_from_db()
        self.assertEqual('3.50', str(self.clothes_1.rating))