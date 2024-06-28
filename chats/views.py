from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from chats.models import OrderMessage
from chats.serializers import OrderMessageSerializer

# Create your views here.
class OrderMessagesViewSet(ViewSet):
  serializer_class=OrderMessageSerializer
  def list(self,request):
    """List order messages"""
    orderMessages=OrderMessage.objects.all()
    serializer=self.serializer_class(instance=orderMessages,many=True)
    return serializer.data