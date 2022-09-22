from distutils.command.upload import upload
import email
from itertools import product
from pyexpat import model

from django.db import models

# Create your models here.

from ecommerce.models import Ciudad, Producto

from bases.models import ClaseModelo




class DatosCliente (ClaseModelo):

    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    ciudad =  models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=300, null=True, blank=True)
    celular = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=350, null=False, blank=False)
    descripcion = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombres)


class Cotizaciones (ClaseModelo):
    razon_social = models.CharField(max_length=100, null=False, blank=False)
    nit = models.CharField(max_length=30, null=True, blank=True)
    celular = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=350, null=False, blank=False)
    total = models.IntegerField(blank=False, null=False)


class Cotizacion_det(ClaseModelo):
     cotizacion = models.ForeignKey(Cotizaciones, on_delete=models.CASCADE)
     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
     cantidad = models.IntegerField(blank=False, null=False)
     sub_total = models.IntegerField(blank=False, null=False)


class Pedido(ClaseModelo):
    
    numPedido = models.IntegerField(blank=False, null=False)
    cliente = models.ForeignKey(DatosCliente, on_delete=models.CASCADE)
    fecha_pedido = models.CharField(max_length=50, null=False, blank=False)
    total_pedido = models.FloatField(blank=True, null=True)
    img_qr = models.ImageField(upload_to = 'static/img/qr')
    img_boucher = models.ImageField(upload_to = 'static/img/boucher')
    estado_atencion =  models.BooleanField(default=True)
    usuario_atencion =  models.IntegerField(blank=True, null=True)
    pedido_finalizado =  models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.numPedido)

class DetallePedido(ClaseModelo):
    
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=False, null=False)

    
