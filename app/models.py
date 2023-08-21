from django.db import models
import datetime

class Seller(models.Model):
    name = models.CharField(max_length=150, default='Behzod Xidirov')
    address = models.CharField(max_length=150, default='Tashkent, Muqumiy 441')
    phone = models.IntegerField(default='+998997101071')
    date = models.DateField(default=datetime.date.today)

class Buyer(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    purchased_date = models.DateField(default=datetime.date.today)

class Product(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
