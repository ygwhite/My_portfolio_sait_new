from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from orders.models import SalesOrder
from orders.serializers import OrderSeralizer
from rest_framework import viewsets
from .models import CartItem
from .serializers import CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSeralizer

def orders_app(request):
    return render(request, 'main.html')

