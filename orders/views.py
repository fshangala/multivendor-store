from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from orders.serializers import OrderSerializer, OrderItemSerializer
from orders.models import Order

# Create your views here.
class OrderViewSet(ViewSet):
  serializer_class=OrderSerializer

  def list(self,request):
    """ List orders """
    orders=Order.objects.all()
    serializer=self.serializer_class(instance=orders,many=True)
    return Response(serializer.data)