from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="Unknown")  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    size = models.CharField(max_length=20, default="Unknown")
