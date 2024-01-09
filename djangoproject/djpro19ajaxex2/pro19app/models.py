from django.db import models

# Create your models here.
class Product(models.Model):
    category=models.IntegerField()
    pname=models.CharField(max_length=20)
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.CharField(max_length=100)
    
def __str__(self):
    return self.pname