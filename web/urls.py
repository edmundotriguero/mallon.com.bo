from django.urls import path
from web.views import inicio, nosotros, info


urlpatterns = [


    path('', inicio, name='index'),
    path('nosotros', nosotros, name='nosotros'),

    path('info', info, name='info'),


]
