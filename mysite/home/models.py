from django.db import models

# Create your models here.

#CRUD operations
class Student(models.Model):
  name=models.CharField(max_length=15)
  age=models.IntegerField()
  email=models.EmailField(null=True,blank=True)
  address=models.TextField(null=True,blank=True)
  # images=models.ImageField()
  # file=models.FileField()
  
class Car(models.Model):
  car_name=models.CharField(max_length=50)
  speed=models.IntegerField(default=50)

  def __str__(self):
    return self.car_name