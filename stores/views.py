from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from stores.models import Store
from stores.serializers import StoreSerializer

# Create your views here.
class StoreViewSet(ViewSet):
  def list(self,request):
    stores=Store.objects.all()
    serializer=StoreSerializer(instance=stores,many=True)
    return Response(serializer.data)

  def retrieve(self,request,pk):
    store=Store.objects.get(pk=pk)
    serializer=StoreSerializer(instance=store)
    return Response(serializer.data)
  
  def create(self,request):
    serializer=StoreSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)