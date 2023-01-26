from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder


class OrderSeralizer(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'
