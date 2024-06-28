from rest_framework import serializers
from orders.models import Order, order_status_choices, Stock
from django.contrib.auth.models import User

class OrderItemSerializer(serializers.Serializer):
  order=serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
  stock=serializers.PrimaryKeyRelatedField(queryset=Stock.objects.all())
  price=serializers.FloatField()
  quantity=serializers.IntegerField()

class OrderSerializer(serializers.Serializer):
  user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  status=serializers.ChoiceField(choices=order_status_choices)
  order_items=OrderItemSerializer(many=True,read_only=True)

