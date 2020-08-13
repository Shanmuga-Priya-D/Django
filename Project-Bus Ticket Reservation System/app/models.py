from django.db import models
from django.conf import settings
# Create your models here.
class Fun(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.name}'

class Contact(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    message=models.TextField(max_length=300)
   
    def __int__(self):
        return self.email
    

class BusInfo(models.Model):
    travel=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    depart=models.CharField(max_length=10)
    fare=models.CharField(max_length=10)
    av_seats=models.IntegerField(blank=True,null=True)
    

        
class Bookings(models.Model):
    user=models.ForeignKey(Fun,on_delete=models.CASCADE)
    fro=models.CharField(max_length=30,blank=True,null=True)
    to=models.CharField(max_length=30,blank=True,null=True)
    dat=models.CharField(max_length=30,blank=True,null=True)
    bus=models.ForeignKey(BusInfo,on_delete=models.CASCADE)
