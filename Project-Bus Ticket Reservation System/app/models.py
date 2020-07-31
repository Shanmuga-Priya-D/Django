from django.db import models

# Create your models here.

class Contact(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    message=models.TextField(max_length=300)
   
    def __int__(self):
        return self.email