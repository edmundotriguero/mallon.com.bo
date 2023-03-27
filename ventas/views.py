from django.shortcuts import render

# Create your views here.
from bases.views import SinPrivilegios

from django.views import generic

from tienda.models import  Pedido



class PedidosView(SinPrivilegios, generic.ListView):
    permission_required = 'pedido.view_inplace'
    model = Pedido
    template_name = 'pedido/pedidos_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'



    