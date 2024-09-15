from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin



# Create your models here.
class User(AbstractUser):
    pass

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_creationTime = models.DateTimeField(auto_now_add=True)
    customer_description = models.CharField(max_length=200)
    customer_state = models.CharField(max_length=50)
    customer_city = models.CharField(max_length=50)
    customer_zipcode = models.IntegerField()
    customer_address = models.CharField(max_length=100)
    customer_address2 = models.CharField(max_length=100, null=True)
    customer_phone = models.IntegerField()
    customer_email = models.EmailField()

class CustomerUser(models.Model):
    cuser_name = models.CharField(max_length=50)
    cuser_creationTime = models.DateTimeField(auto_now_add=True)
    cuser_superuser = models.BooleanField(default=False)
    

admin.site.register(User)
admin.site.register(Customer)
