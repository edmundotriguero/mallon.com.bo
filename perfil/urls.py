from django.urls import path


# importar para las vistas de login
from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views

from perfil.views import profile, cotizaciones, pedidos, pedido_detalle_view

 

urlpatterns = [


    

    path('index',profile,name='index'),
    path('cotizaciones',cotizaciones,name='cotizaciones'),
    path('pedidos',pedidos,name='pedidos'),
   
    path('pedidos/detalle/<int:id>', pedido_detalle_view, name='pedido_detalle_view'), # ajax
# #     ruta para panel de informacion
#     path('dashboard', Dashboard, name='dashboard'),
]