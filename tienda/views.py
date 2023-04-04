import email
from email.message import EmailMessage
#from math import prod
from multiprocessing import context

from re import template
from urllib.request import Request
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from ecommerce.Carrito import Carrito

from ecommerce.models import Color, Producto, Galeria
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

from bases.utils import send_email_generic

import os
import json
from django.conf import settings

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from ecommerce import context_processor 

from django.contrib.auth.models import BaseUserManager, Group, User

from bases.forms import CustomUserCreationForm
from ecommerce.models import Parametros


from datetime import datetime

from django.contrib.auth import authenticate, login

import string
import random

def tienda(request):
    template_name = 'tienda/tienda.html'
    contexto = {}

    if request.method == 'GET':
        obj = Producto.objects.filter(estado=True).all().order_by('-orden')
        param = Parametros.objects.filter(estado=True, pcorr1=11,pcorr2=1,pnum1=1).get()



        param2 = Parametros.objects.filter(pcorr1=12,pcorr2=1).get()

        inicio = param2.ptxt1
        fin = param2.ptxt2

        obj = obj[int(inicio)-1:int(fin)]




        contexto = {'obj':obj,'param':param, 'inicio':inicio, 'fin':fin}

    return render(request, template_name, contexto)




# para usar con ajax
def tienda_recarga(request):
    template_name = 'tienda/tienda.html'


    param = Parametros.objects.filter(pcorr1=12,pcorr2=1).get()




    cantidad = param.ptxt2


    print(cantidad)

    if request.is_ajax():

        inicio_get = int(request.GET.get('inicio')) + int(cantidad)
        fin_get = int(request.GET.get('fin')) + int(cantidad)

        # print(inicio_get)
        # print(fin_get)


        productos = Producto.objects.filter(estado=True).all().order_by('-orden')

        list_data = []


        for indice, valor in enumerate(productos[inicio_get:fin_get+1]):

            # print("++=============================")
            # print(indice)
            # print(valor.id)
            # print(valor.nombre)
            # print(str(valor.img))

            prod = {}
            prod["id"] = valor.id
            prod["nombre"] = valor.nombre
            prod["desc"] = valor.descripcion
            prod["precio"] = valor.precio
            prod["img"] = str(valor.img)

            list_data.append(prod)
       
        
        inicio = int(inicio_get) 
        fin = int(fin_get)  

        data = {
            'inicio': inicio,
            'fin': fin,
            'length':'20',
            'objects':'ok',
            'state':'OK',
            'list_data':list_data

        }

        return HttpResponse(json.dumps(data), 'aplication/json')



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

            if not request.user.is_authenticated:
                password = randon_password()
                email = request.POST.get("email")
                nombres_cliente = request.POST.get("nombres")  + " " + request.POST.get("apellidos")
                formulario = CustomUserCreationForm(data={'username':email,'email':email,'password1':password,'password2':password})

                user_new = formulario.save()
                group = Group.objects.get(name='cliente')
                user_new.groups.add(group)
                user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
                login(request, user)


                #send_email_generic(request,email,"Prueba correo desde un generico","mensaje desde otra clase")

                param = Parametros.objects.filter(pcorr1=10,pcorr2=2).get()
                body_html = param.pclob1.replace("|nombre_cliente|",nombres_cliente)
                body_html = body_html.replace("|email|",email)
                body_html = body_html.replace("|password|",password)

                send_mail(
                    param.ptxt1,
                    None,
                    EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    html_message=body_html) 



            
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
            pedido.fecha_pedido = datetime.now().strftime("%d/%m/%Y")
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
    obj_galeria = []

    if prod.flag_galeria:
        obj_galeria = Galeria.objects.filter(producto=prod.id,estado=True).all().order_by('orden')


    if prod.flag_color :
        colores = prod.col.split(',')

        for i in colores:
            #print(i.strip())

            color = Color.objects.get(pk=i.strip())

            obj_col.append(color.hexadecimal)


   # print(prod.col.split())    

   # print(prod)

    obj = {'prod':prod, 'colores':obj_col, 'galeria':obj_galeria}


    return render(request, template_name, obj)


## Guardar datos de cotizciones


def cotizacionNew(request):
    template_name = 'cliente/cliente_cot_form.html'
    model = Cotizaciones
    
    if request.method == 'POST':
        form = CotizacionesForm(request.POST)

        if form.is_valid():
           
            password = randon_password()

            print(password)
            if not request.user.is_authenticated:
            
                email = request.POST.get("email")
                razon_social = request.POST.get("razon_social")
                formulario = CustomUserCreationForm(data={'username':email,'email':email,'password1':password,'password2':password})

                user_new = formulario.save()
                group = Group.objects.get(name='cliente')
                user_new.groups.add(group)
                user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
                login(request, user)


                #send_email_generic(request,email,"Prueba correo desde un generico","mensaje desde otra clase")

                param = Parametros.objects.filter(pcorr1=10,pcorr2=1).get()
                body_html = param.pclob1.replace("|nombre_cliente|",razon_social)
                body_html = body_html.replace("|email|",email)
                body_html = body_html.replace("|password|",password)

                send_mail(
                    param.ptxt1,
                    None,
                    EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    html_message=body_html)
                #send_mail.send()

                # group = Group.objects.get(name='cliente')
                # user = User('')
                # user.set_password(password)
                # user.groups.add(group)
                # user.is_admin = False
                # user.save()

                
            
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


        else :
            return render(request, template_name, {'form':form})            



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



def randon_password():
    number_of_strings = 5
    length_of_string = 8
    string_randon = ''
    for x in range(number_of_strings):
        string_randon = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))      

    return string_randon