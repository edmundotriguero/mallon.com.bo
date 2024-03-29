from django import forms

from .models import Categoria, SubCategoria, Marca, Color, Producto, Ciudad, Parametros, Galeria, Testimonio






class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['producto','nombre','img','orden','estado']
        
        # widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ParametrosForm(forms.ModelForm):
    class Meta:
        model = Parametros
        fields = ['pcorr1', 'pcorr2', 'pnum1', 'pnum2', 'pdesc', 'ptxt1', 'ptxt2', 'pclob1', 'pclob2', 'estado']

        #widget = {'des': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


# formulario para categorias
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'estado']

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoria
        fields = ['nombre', 'descripcion', 'estado']

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'descripcion', 'estado']

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['nombre', 'descripcion', 'hexadecimal', 'estado']

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'estado', 'flag_precio', 'precio', 'p_inicial', 'p_final', 'img', 'categoria',
                  'flag_subcategoria', 'sub_cat', 'flag_marca', 'brand', 'flag_color', 'col', 'flag_unidadmedida', 'unidad_medida','orden','flag_galeria']

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


# formulario para categorias
class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'estado']

        #widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['persona_testimonio', 'descripcion', 'estado']

        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})