from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render


from django.views import generic
from django.urls import reverse_lazy
 
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# importacion pra la vista basada en funciones
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.http import HttpResponse
from ecommerce.models import Categoria,SubCategoria,Marca,Color,Producto, Ciudad, Parametros

from bases.views import SinPrivilegios



from django.contrib.auth.models import User

from ecommerce.Carrito import Carrito
from .forms  import CategoriaForm, SubCategoriaForm, MarcaForm, ColorForm, ProductoForm,CiudadForm, ParametrosForm

from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


# inicio parametrizacion 

class ParametroView(SinPrivilegios, generic.ListView):
    permission_required = 'parametros.view_inplace'
    model = Parametros
    template_name = 'parametros/parametro_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ParametroNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Parametros
    template_name = 'parametros/parametro_form.html'
    context_object_name = 'obj'
    form_class = ParametrosForm
    success_url = reverse_lazy('ecommerce:parametro_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class ParametroEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Parametros
    template_name = 'parametros/parametro_form.html'
    context_object_name = 'obj' 
    form_class = ParametrosForm
    success_url = reverse_lazy('ecommerce:parametro_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def parametro_disabled(request, id):

    

    template_name = 'parametros/parametro_disabled.html'
    contexto = {}
    obj = Parametros.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)


# fin parametrizacion 





class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = 'categoria.view_inplace'
    model = Categoria
    template_name = 'categoria/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'categoria/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('ecommerce:categoria_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'categoria/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('ecommerce:categoria_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def categoria_disabled(request, id):

    

    template_name = 'categoria/categoria_disabled.html'
    contexto = {}
    obj = Categoria.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)


#vistas para subcategorias

class SubcategoriaView(SinPrivilegios, generic.ListView):
    permission_required = 'subcategoria.view_inplace'
    model = SubCategoria
    template_name = 'subcategoria/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class SubcategoriaNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = 'subcategoria/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('ecommerce:subcategoria_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class SubcategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = 'subcategoria/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('ecommerce:subcategoria_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def subcategoria_disabled(request, id):

    

    template_name = 'subcategoria/subcategoria_disabled.html'
    contexto = {}
    obj = SubCategoria.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)


    # Vistas para Marca

class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = 'marca.view_inplace'
    model = Marca
    template_name = 'marca/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class MarcaNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'marca/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('ecommerce:marca_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class MarcaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'marca/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('ecommerce:marca_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def marca_disabled(request, id):

    

    template_name = 'marca/marca_disabled.html'
    contexto = {}
    obj = Marca.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)


# vistas para colores 


class ColorView(SinPrivilegios, generic.ListView):
    permission_required = 'color.view_inplace'
    model = Color
    template_name = 'color/color_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ColorNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Color
    template_name = 'color/color_form.html'
    context_object_name = 'obj'
    form_class = ColorForm
    success_url = reverse_lazy('ecommerce:color_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class ColorEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Color
    template_name = 'color/color_form.html'
    context_object_name = 'obj'
    form_class = ColorForm
    success_url = reverse_lazy('ecommerce:color_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def color_disabled(request, id):

    

    template_name = 'color/color_disabled.html'
    contexto = {}
    obj = Color.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)


# vistas para productos


class ProductoView(SinPrivilegios, generic.ListView):
    permission_required = 'producto.view_inplace'
    model = Producto
    template_name = 'producto/producto_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class ProductoNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'producto/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('ecommerce:producto_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class ProductoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'producto/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('ecommerce:producto_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def producto_disabled(request, id):

    

    template_name = 'producto/producto_disabled.html'
    contexto = {}
    obj = Producto.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)


# vistas para adm ciudad


class CiudadView(SinPrivilegios, generic.ListView):
    permission_required = 'ciudad.view_inplace'
    model = Ciudad
    template_name = 'ciudad/ciudad_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

class CiudadNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Ciudad
    template_name = 'ciudad/ciudad_form.html'
    context_object_name = 'obj'
    form_class = CiudadForm
    success_url = reverse_lazy('ecommerce:ciudad_list')
    login_url = 'bases:login'
    success_message = "Creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_created = self.request.user

        return super().form_valid(form)


class CiudadEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Ciudad
    template_name = 'ciudad/ciudad_form.html'
    context_object_name = 'obj'
    form_class = CiudadForm
    success_url = reverse_lazy('ecommerce:ciudad_list')
    login_url = 'bases:login'
    success_message = "Actializado satisfactoriamente"

    def form_valid(self, form):
        form.instance.user_updated = self.request.user.id

        return super().form_valid(form)


def ciudad_disabled(request, id):

    

    template_name = 'ciudad/ciudad_disabled.html'
    contexto = {}
    obj = Ciudad.objects.filter(pk=id).first()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

    if request.method == 'POST':
        obj.estado = False
        obj.save()
        # mensaje par que la vista lo muestre sin coloca en comentarios pues al momento de los esta haciendo con ajax
        # messages.success(request, 'Se inactivo correctamente')

        contexto = {'obj': 'OK'}
        return HttpResponse('Registro inactivo')

    return render(request, template_name, contexto)



# fin vistas para adm ciudad




# Vistas para carrito 

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda:tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda:tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda:tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda:tienda")




def guardar_compra(request):
    #carrito = Carrito(request)
    car_impl = request.session.get("carrito")
    print(car_impl)
    print(type(car_impl))
    i = 1;

    for  car  in car_impl.values():

        print(car['nombre'])
        print(type(car))
        i = i +1
    
    return redirect("tienda:tienda")
