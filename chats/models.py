from django.db import models
from orders.models import Order
from django.contrib.auth.models import User

# Create your models here.
class OrderMessage(models.Model):
  user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='order_messages')
  order=models.ForeignKey(to=Order,on_delete=models.CASCADE,related_name='order_messages')
  message=models.TextField()