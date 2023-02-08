from django.shortcuts import render

# Create your views here.

from tienda.models import Cotizaciones



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