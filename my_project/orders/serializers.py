from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder
from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('item_id', 'quantity')


class OrderSeralizer(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'
