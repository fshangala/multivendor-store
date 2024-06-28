from django.db import models
from django.contrib.auth.models import User
from products.models import Stock

# Create your models here.
order_status_choices=(
  ('DRAFT','DRAFT'),
  ('SUBMITTED','SUBMITTED'),
  ('APPROVED','APPROVED'),
  ('COMPLETE','COMPLETE'),
)
class Order(models.Model):
  user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='orders')
  status=models.CharField(max_length=200,choices=order_status_choices,default='DRAFT')

class OrderItem(models.Model):
  order=models.ForeignKey(to=Order,on_delete=models.CASCADE,related_name='order_items')
  stock=models.ForeignKey(to=Stock,on_delete=models.CASCADE,related_name='order_items')
  price=models.FloatField()
  quantity=models.IntegerField()

  
