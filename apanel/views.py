from multiprocessing import context
from urllib import request
from django.shortcuts import render


from django.views import generic
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# importacion pra la vista basada en funciones
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.http import HttpResponse
from apanel.models import Slider

from bases.views import SinPrivilegios

from django.contrib.auth.models import User


from apanel.forms  import SliderForm

from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required(login_url='/b/login/')
@permission_required('', login_url='bases:sin_privilegios')
def dashboard(request):
    template_name = 'dashboard.html'
    contexto = {}

    return render(request, template_name, contexto)



class SliderView(SinPrivilegios, generic.ListView):
    permission_required = 'slider.view_inplace'
    model = Slider
    template_name = 'slider/slider_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class SliderNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Slider
    template_name = 'slider/slider_form.html'
    context_object_name = 'obj'
    form_class = SliderForm
    success_url = reverse_lazy('apanel:slider_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class SliderEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Slider
    template_name = 'slider/slider_form.html'
    context_object_name = 'obj'
    form_class = SliderForm
    success_url = reverse_lazy('apanel:slider_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def slider_disabled(request, id):

    print("slider disables")

    template_name = 'slider/slider_disabled.html'
    contexto = {}
    obj = Slider.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)
