from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

from bases.models import ClaseModelo


class Categoria (ClaseModelo):

    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class SubCategoria (ClaseModelo):

    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)



class Marca (ClaseModelo):

    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Color (ClaseModelo):
 
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    hexadecimal = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Producto(ClaseModelo):

    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    flag_precio = models.BooleanField(blank=False, null=False)
    precio =  models.FloatField(blank=True, null=True)
    p_inicial = models.IntegerField(blank=True, null=True)
    p_final = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to = 'static/img/productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    flag_subcategoria =  models.BooleanField(blank=False, null=False)
    sub_cat = models.CharField(max_length=100, null=True, blank=True)
    flag_marca =  models.BooleanField(blank=False, null=False)
    brand = models.CharField(max_length=100, null=True, blank=True)
    flag_color =  models.BooleanField(blank=False, null=False)
    col = models.CharField(max_length=100, null=True, blank=True)
    flag_unidadmedida = models.BooleanField(blank=False, null=False)
    unidad_medida = models.CharField(max_length=100, null=True, blank=True)


class Carro(ClaseModelo):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=False, null=False)
    

class Ciudad (ClaseModelo):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return '{}'.format(self.nombre)