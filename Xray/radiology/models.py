from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class DocumentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    description = models.TextField()
    image = models.ImageField(upload_to='reports/')
    file = models.FileField(upload_to='documents/')

class DoctorsInfo(models.Model):
    Link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    DoctorName= models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    Location = models.CharField(max_length=500)
    Specialiter = models.CharField(max_length=500)
    def __str__(require):
        return require.DoctorName