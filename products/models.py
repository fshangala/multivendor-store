from django.db import models
from stores.models import Store

# Create your models here.
class Product(models.Model):
  store=models.ForeignKey(to=Store,on_delete=models.CASCADE,related_name='products')
  name=models.CharField(max_length=200)
  description=models.TextField()

  def __str__(self):
    return self.name

class Stock(models.Model):
  product=models.ForeignKey(to=Product,on_delete=models.CASCADE,related_name='stocks')
  quantity=models.IntegerField()
  total_price=models.FloatField()
  sale_price_per_item=models.FloatField()

  def __str__(self):
    return self.sale_price_per_item