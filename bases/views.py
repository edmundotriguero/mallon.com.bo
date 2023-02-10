from multiprocessing import context
from re import template
from tokenize import group
from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin ,  PermissionRequiredMixin
# Create your views here.
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import Group


from django.contrib.auth.views import LoginView



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



def registro(request):
    template = 'bases/registration.html'
    obj = { 'form':CustomUserCreationForm }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            
            user_new = formulario.save()
            group = Group.objects.get(name='cliente')
            user_new.groups.add(group)
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            print('Redirigiendo')
            return redirect('web:index')
        

    return render(request, template,obj)



# class Login(LoginView):
#     authentication_form = CustomAuthenticationForm

#     form_class = CustomAuthenticationForm

#     template_name = 'login.html'

#     def form_valid(self, form):

#         #remember_me = form.cleaned_data['remember_me']

#         login(self.request, form.get_user())

#         user = form.get_user()

#         group = user.groups

#         print(group)    
#         # if remember_me:

#         #     self.request.session.set_expiry(1209600)

#         return super(LoginView, self).form_valid(form)


def profile(request):
    template_name = 'bases/profile.html'
    contexto = {}

    return render(request, template_name, contexto)