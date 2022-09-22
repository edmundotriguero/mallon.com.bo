from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

from bases.models import ClaseModelo




class Slider (ClaseModelo):

    nombre = models.CharField(max_length=100, null=False, blank=False)
    img = models.ImageField(upload_to = 'rondas')
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    orden = models.IntegerField(blank=False, null=False)


