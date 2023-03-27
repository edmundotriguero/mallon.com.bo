from django.urls import path
from .views import  PedidosView




urlpatterns = [


    # rutas para administrar parametrizacion.

    path('pedidos/view', PedidosView.as_view(), name='pedidos_list'),
    # path('parametro/new', ParametroNew.as_view(), name='parametro_new'),
    # path('parametro/edit/<int:pk>', ParametroEdit.as_view(), name='parametro_edit'),
    # path('parametro/disabled/<int:id>', parametro_disabled, name='parametro_disabled'), # ajax


]