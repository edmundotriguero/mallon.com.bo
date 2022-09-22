from multiprocessing import context
from urllib import request
from django.shortcuts import render

from apanel.models import Slider

# Create your views here.


def inicio(request):
    template_name = 'web/index.html'
    contexto = {}

    if request.method == 'GET':
        obj = Slider.objects.filter(estado=True).all().order_by('orden')

        contexto = {'obj':obj}

    return render(request, template_name, contexto)




def nosotros(request):
    template_name = 'web/nosotros.html'
    contexto = {}

    return render(request, template_name, contexto)


def info(request):
    template_name = 'web/info.html'
    contexto = {}

    return render(request, template_name, contexto)