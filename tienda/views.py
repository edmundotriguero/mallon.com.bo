import email
from email.message import EmailMessage
from math import prod
from multiprocessing import context

from re import template
from urllib.request import Request
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from ecommerce.Carrito import Carrito

from ecommerce.models import Color, Producto
from .forms import DatosClienteForm, CotizacionesForm

from .models import DatosCliente, DetallePedido, Pedido, Cotizaciones, Cotizacion_det
# Create your views here.
from django.views import generic

from bases.views import SinPrivilegios
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin

# configuracion para email
from django.core.mail import send_mail
from mallon.settings import EMAIL_HOST_USER


import os
from django.conf import settings

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from ecommerce import context_processor 


def tienda(request):
    template_name = 'tienda/tienda.html'
    contexto = {}

    if request.method == 'GET':
        obj = Producto.objects.filter(estado=True).all()

        contexto = {'obj':obj}

    return render(request, template_name, contexto)


# class DatosClienteNew(generic.CreateView):
#     model = DatosCliente
#     template_name = 'cliente/cliente_form.html'
#     context_object_name = 'obj'
#     form_class = DatosClienteForm
#     success_url = reverse_lazy('tienda:tienda')
#     #login_url = 'bases:login'
#     success_message = "Creado satisfactoriamente"

#     def form_valid(self, form):
        

#         form.instance.user_created = self.request.user

#         return super().form_valid(form)


def finPedido( request):
    template_name = 'tienda/tienda_fin_pedido.html'

   # print (pk)

    return render(request, template_name)


def datosClienteNew(request):
    template_name = 'cliente/cliente_form.html'
    model = DatosCliente
    
    if request.method == 'POST':
        form = DatosClienteForm(request.POST)

        if form.is_valid():
            
            # Guarda los datos del cliente 
            client = form.save(commit=False)
            client.user_created = request.user
            client.save()
            print(type(client))
            print(client.pk)
            print(client.email)

            # Guarda la cabecera del pedido

            pedido = Pedido()

            pedido.numPedido = client.pk + 50000
            pedido.cliente = client
            pedido.fecha_pedido = "19/08/2022"
            pedido.user_created = request.user
            pedido.save()
            

            print("Pedido")
            print(pedido.pk)
            # Guarda los detalles del pedido

            detalle = request.session.get("carrito")

            print(type(detalle)) 

            for val in detalle.values():

                print(val['producto_id'])            
            
            
            carrito = Carrito(request)
            carrito.limpiar()

       

            # #TODO MEJORAR EL PROCESO DE ENVIO DE CORREO 
            #try:
            # send_mail(
            #     "MALLON.COM.BO Detalle de su pedido ",
            #     "Estimado Cliente su pedido fue recibido de forma exitosa. En un momento nos contactaremos con usted",
            #     EMAIL_HOST_USER,
            #     [client.email],
            #      fail_silently=False,
            # )
            #send_mail.send()
            
            return redirect('tienda:fin_pedido') 
            
            # except:
            #     return redirect('tienda:fin_pedido') 






    else:
        form = DatosClienteForm()
    return render(request, template_name, {'form':form})


def producto_view( request, pk):
    template_name = 'tienda/producto.html'

    prod = Producto.objects.get(pk=pk)

    obj_col = []

    if prod.flag_color :
        colores = prod.col.split(',')

        for i in colores:
            #print(i.strip())

            color = Color.objects.get(pk=i.strip())

            obj_col.append(color.hexadecimal)


   # print(prod.col.split())    

   # print(prod)

    obj = {'prod':prod, 'colores':obj_col}


    return render(request, template_name, obj)


## Guardar datos de cotizciones


def cotizacionNew(request):
    template_name = 'cliente/cliente_cot_form.html'
    model = Cotizaciones
    
    if request.method == 'POST':
        form = CotizacionesForm(request.POST)

        if form.is_valid():
            
            total = context_processor.total_carrito(request)
           
            # Guarda los datos del cliente 
            client = form.save(commit=False)
            client.user_created = request.user
            client.total = total['total_carrito']
            client.save()
            print(type(client))
            print(client.pk)
            print(client.email)

            # Guarda la cabecera del pedido

           

            
            

            
            # Guarda los detalles del pedido

            detalle = request.session.get("carrito")

           

            for val in detalle.values():
                print(val['producto_id'])   
                cot = Cotizacion_det()

                producto = Producto.objects.get(pk = val['producto_id'])

                cot.producto = producto
                cot.cotizacion = client
                cot.cantidad = val['cantidad']
                cot.sub_total = val['acumulado']
                cot.user_created = request.user 
                cot.save()
            
            

       

            try:
                template = get_template('tienda/cotizacion_pdf.html')

                context = {'cliente':client}
                html = template.render(context)
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="cotizacion.pdf"'
                pisaStatus = pisa.CreatePDF(
                    html, dest=response
                ) 
        
                carrito = Carrito(request)
                carrito.limpiar()

                return response

            except:
                pass

            return HttpResponseRedirect(reverse_lazy('tienda'))


            # #TODO MEJORAR EL PROCESO DE ENVIO DE CORREO 
            #try:
            # send_mail(
            #     "MALLON.COM.BO Detalle de su pedido ",
            #     "Estimado Cliente su pedido fue recibido de forma exitosa. En un momento nos contactaremos con usted",
            #     EMAIL_HOST_USER,
            #     [client.email],
            #      fail_silently=False,
            # )
            #send_mail.send()
            
            #return redirect('tienda:fin_pedido') 
            
            # except:
            #     return redirect('tienda:fin_pedido') 






    else:
        form = CotizacionesForm()
    return render(request, template_name, {'form':form})

## fin datos cotizciones



def cotizacion_download(request):


    # try:
    #     template = get_template('tienda/cotizacion_pdf.html')

    #     context = {'title':'Cotizacion Mallon'}
    #     html = template.render(context)
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="cotizacion.pdf"'
    #     pisaStatus = pisa.CreatePDF(
    #         html, dest=response
    #     ) 
        
    #     return response

    # except:
    #     pass

    # return HttpResponseRedirect(reverse_lazy('tienda'))

    
    return render(request, 'tienda/cotizacion_pdf.html')