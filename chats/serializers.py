from rest_framework import serializers
from chats.models import OrderMessage
from orders.models import Order

class OrderMessageSerializer(serializers.Serializer):
  user=serializers.PrimaryKeyRelatedField(queryset=OrderMessage.objects.all())
  order=serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
  message=serializers.CharField()