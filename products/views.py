from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from products.models import Product, Stock
from products.serializers import ProductSerializer, StockSerializer
from rest_framework.response import Response

# Create your views here.
class ProductViewSet(ViewSet):
  def list(self,request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)
  
  def retrieve(self,request,pk):
    product=Product.objects.get(pk=pk)
    serializer=ProductSerializer(instance=product)
    return serializer.data
  
  def create(self,request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

class StockViewSet(ViewSet):
  def list(self,request):
    stocks=Stock.objects.all()
    serializer=StockSerializer(instance=stocks,many=True)
    return Response(serializer.data)
  
  def retrieve(self,request,pk):
    stock=Stock.objects.get(pk=pk)
    serializer=StockSerializer(instance=stock)
    return serializer.data
  
  def create(self,request):
    serializer=StockSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
