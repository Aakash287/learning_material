from django.db import models

# Create your models here.



class Details(models.Model):

    name= models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=200)
    number=models.BigIntegerField()
    address=models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', null=True)
    image = models.ImageField(upload_to='images/', null=True)