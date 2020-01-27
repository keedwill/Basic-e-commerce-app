from django.db import models
from datetime import datetime


# Create your models here.


class Soap(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class OrderList(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    no_of_item = models.IntegerField()
    email = models.EmailField(default=False)
    product_name = models.CharField(max_length=20,default=False)
    product_price = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
    unit_cost = models.IntegerField(default=False)
    uuid = models.CharField(max_length=50,default=False)
