from django import forms

from .models import Slider, Sticker

# formulario para categorias
class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['nombre','img','descripcion','orden','estado']
        
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})




class StickerForm(forms.ModelForm):
    class Meta:
        model = Sticker
        fields = ['nombre','img','descripcion','orden','estado']
        
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})