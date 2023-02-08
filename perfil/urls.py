from django.urls import path

from perfil.views import profile, cotizaciones

# importar para las vistas de login
from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views


 

urlpatterns = [


    

    path('index',profile,name='index'),
    path('cotizaciones',cotizaciones,name='cotizaciones'),
   
    
# #     ruta para panel de informacion
#     path('dashboard', Dashboard, name='dashboard'),
]