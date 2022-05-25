from django.db import models

# Create your models here.

from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()



class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)


class Sellers(models.Model):
    phone = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)


class Warehouses(models.Model):
    city = models.CharField(max_length=200)
    number=models.PositiveIntegerField()


