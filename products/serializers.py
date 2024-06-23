from rest_framework import serializers
from products.models import Product, Stock
from stores.models import Store

class StockSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  product=serializers.PrimaryKeyRelatedField(queryset=Stock.objects.all(),required=True)
  quantity=serializers.IntegerField(required=True)
  total_price=serializers.FloatField(required=True)
  sale_price_per_item=serializers.FloatField(required=True)

  def create(self,validated_data):
    stock=Stock.objects.create(**validated_data)
    return stock


class ProductSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  store=serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
  name=serializers.CharField(required=True)
  description=serializers.CharField(required=True)

  stocks=StockSerializer(many=True,read_only=True)

  def create(self,validated_data):
    #validated_data['store']=Store.objects.get(pk=validated_data['store'])
    product=Product.objects.create(**validated_data)
    return product
  