from django import forms

from .models import Ciudad, DatosCliente,Cotizaciones

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



class DatosClienteForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = DatosCliente
        
        fields = ['nombres','apellidos','ciudad','direccion','celular','email','descripcion']
        
        #widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})



class CotizacionesForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Cotizaciones
        
        fields = ['razon_social','nit','celular','email']
        
        #widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
