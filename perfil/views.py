from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from tienda.models import Cotizaciones, Pedido, DetallePedido


def profile(request):
    template_name = 'perfil/index.html'

    user = request.user

    print(user)

    contexto = {}

    return render(request, template_name, contexto)


def cotizaciones(request):
    template_name = 'perfil/cotizaciones.html'

    user = request.user.pk
    #print(user.pk)
    cot = Cotizaciones.objects.filter(user_created=user).all()

    print(cot)

    

    contexto = {'obj':cot}

    return render(request, template_name, contexto)    


def pedidos(request):
    template_name = 'pedido/pedidos.html'

    user = request.user.pk
    #print(user.pk)
    cot = Pedido.objects.filter(user_created=user).all()

    print(cot)

    

    contexto = {'obj':cot}

    return render(request, template_name, contexto)    

def pedido_detalle_view(request, id):

    

    template_name = 'pedido/pedido_detalle_view.html'
    contexto = {}

    pedido = Pedido.objects.filter(id=id).get()
    obj = DetallePedido.objects.filter(pedido_id=id).all()

    #if not obj:
     #   return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj,'pedido':pedido}

   
        

     

    return render(request, template_name, contexto)