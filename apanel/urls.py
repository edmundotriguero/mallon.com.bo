from django.urls import path
from apanel.views import dashboard, SliderView, SliderNew, SliderEdit, slider_disabled



urlpatterns = [


    path('', dashboard, name='dashboard'),
    

# rutas para administrar Sliders.

    path('slider/', SliderView.as_view(), name='slider_list'),

    path('slider/new', SliderNew.as_view(), name='slider_new'),

    path('slider/edit/<int:pk>', SliderEdit.as_view(), name='slider_edit'),

    path('slider/disabled/<int:id>', slider_disabled, name='slider_disabled'), # ajax

    


]
