from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="Unknown")  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    size = models.CharField(max_length=20, default="Unknown")

    def __str__(self):
        return self.name

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.item.price
