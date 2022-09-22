from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin ,  PermissionRequiredMixin
# Create your views here.


def inicio(request):
    template_name = 'bases/index.html'
    contexto = {}

    return render(request, template_name, contexto)




class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = 'redirecto_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))



class HomesinPrivilegios(generic.TemplateView):
    template_name="bases/error_400.html"