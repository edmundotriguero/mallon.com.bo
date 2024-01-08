from multiprocessing import context
from urllib import request
from django.shortcuts import render

from apanel.models import Slider, Sticker

from ecommerce.models import Parametros, Testimonio

# Create your views here.


def inicio(request):
    template_name = 'web/index.html'
    contexto = {}

    if request.method == 'GET':
        obj = Slider.objects.filter(estado=True).all().order_by('orden')


        stick = Sticker.objects.filter(estado=True).all().order_by('orden')

        testimonios = Testimonio.objects.filter(estado=1).all().order_by("id")


        param =  Parametros.objects.filter(estado=True, pcorr1=13,pcorr2=1,pnum1=1).get()

        param_num = param.pnum2

        contexto = {'obj':obj,'stick':stick,'num_marca':param_num,"testimonios":testimonios}

    return render(request, template_name, contexto)




def nosotros(request):
    template_name = 'web/nosotros.html'
    contexto = {}

    return render(request, template_name, contexto)


def info(request):
    template_name = 'web/info.html'
    contexto = {}

    return render(request, template_name, contexto)