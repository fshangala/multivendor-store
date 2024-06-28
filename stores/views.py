from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import permissions
from stores.models import Store
from stores.serializers import StoreSerializer
from drf_spectacular.utils import extend_schema
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# Create your views here.
class StoreViewSet(ViewSet):
  """ Store endpoint """
  serializer_class=StoreSerializer
  permission_classes=[permissions.IsAuthenticated,TokenHasReadWriteScope]

  def list(self,request):
    """ List stores """
    stores=Store.objects.all()
    serializer=StoreSerializer(instance=stores,many=True)
    return Response(serializer.data)
    
  def retrieve(self,request,pk):
    """
    Retrieve a single Store by Primary key
    """
    store=Store.objects.get(pk=pk)
    serializer=StoreSerializer(instance=store)
    return Response(serializer.data)
  
  def create(self,request):
    """ Create a Store """
    serializer=StoreSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  
  def destroy(self,request,pk):
    """ Delete the store """
    store = Store.objects.get(pk=pk)
    result = store.delete()
    return Response(result)