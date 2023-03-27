from django.urls import path
from tienda.views import tienda, datosClienteNew, finPedido, producto_view, cotizacion_download, cotizacionNew, tienda_recarga


urlpatterns = [


    path('', tienda, name='tienda'),

    path('tienda/loader', tienda_recarga),
    #path('nosotros', nosotros, name='nosotros'),
    path('cliente/new', datosClienteNew, name='cliente_new'),
    #path('info', info, name='info'),
    path('finpedido', finPedido, name='fin_pedido'),

    path('producto/<int:pk>/', producto_view, name='producto_id'),


    path('cotizaciones/new', cotizacionNew, name='cotizacion_new'),

    path('cotizacion/pdf', cotizacion_download, name='cotizacion_pdf' )

]
