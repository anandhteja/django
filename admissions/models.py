from django.db import models
from django.urls import reverse

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    classname=models.IntegerField()
    contact_number=models.CharField(max_length=15)


class Teacher(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    
    contact_number=models.CharField(max_length=15)
    
    

