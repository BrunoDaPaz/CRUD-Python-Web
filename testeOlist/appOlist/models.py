from django.db import models
# Create your models here.
class Sellers(models.Model):
    name = models.CharField(max_length=150)
    socialReason = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=150)

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    value = models.IntegerField()
    category = models.CharField(max_length=100)

class Marketplaces(models.Model):
    name = models.CharField(max_length=150)
    socialReason = models.CharField(max_length=150)
    site = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=150)

class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)