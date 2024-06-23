from rest_framework import serializers
from stores.models import Store

class StoreSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  name=serializers.CharField(required=True)
  description=serializers.CharField(required=True)

  def create(self,validated_data):
    store=Store.objects.create(**validated_data)
    return store