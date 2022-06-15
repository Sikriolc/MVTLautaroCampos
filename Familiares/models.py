from django.db import models
from django.forms import CharField, DateField

class Familia(models.Model):

    nombre= models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    annonacimiento=models.DateField()
    parentezco=models.CharField(max_length=10)
