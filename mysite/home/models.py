from django.db import models

# Create your models here.

class Student(models.Model):
  name=models.CharField(max_length=15)
  age=models.IntegerField()
  email=models.EmailField(null=True,blank=True)
  address=models.TextField(null=True,blank=True)
  # images=models.ImageField()
  # file=models.FileField()
  
class Product(models.Model):
  pass