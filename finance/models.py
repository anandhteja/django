from django.db import models
from django.urls import reverse


# Create your models here.


class Fee(models.Model):
    Student_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    class_name=models.IntegerField()
    contact_number=models.CharField(max_length=50)
    fee_due=models.IntegerField()




class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created=models.CharField(max_length=50)
    photo=models.ImageField( upload_to='images/')

  