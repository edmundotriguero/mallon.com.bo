from django.urls import path
from .views import  CategoriaView, CategoriaNew, CategoriaEdit, categoria_disabled,\
    SubcategoriaView,SubcategoriaNew,SubcategoriaEdit, subcategoria_disabled,\
        MarcaView,MarcaNew, MarcaEdit,marca_disabled,\
            ColorView, ColorNew, ColorEdit, color_disabled,\
                ProductoView, ProductoNew, ProductoEdit, producto_disabled,\
                    agregar_producto, eliminar_producto, restar_producto, limpiar_carrito,\
                        CiudadNew, CiudadView, CiudadEdit, ciudad_disabled,\
                        guardar_compra,\
                        ParametroView, ParametroNew, ParametroEdit, parametro_disabled,\
                        galeria_view, GaleriaNew, galeria_disabled,\
                        TestimonioView, TestimonioNew, TestimonioEdit, testimonio_disabled




urlpatterns = [




    # rutas para administrar categorias.

    path('galeria/<int:pk>', galeria_view, name='galeria_list'),
    path('galeria/new/<int:id>', GaleriaNew.as_view(), name='galeria_new'),
    # path('categoria/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('galeria/disabled/<int:id>', galeria_disabled, name='galeria_disabled'), # ajax

    # rutas para administrar parametrizacion.

    path('parametro/', ParametroView.as_view(), name='parametro_list'),
    path('parametro/new', ParametroNew.as_view(), name='parametro_new'),
    path('parametro/edit/<int:pk>', ParametroEdit.as_view(), name='parametro_edit'),
    path('parametro/disabled/<int:id>', parametro_disabled, name='parametro_disabled'), # ajax

    
    

# rutas para administrar categorias.

    path('categoria/', CategoriaView.as_view(), name='categoria_list'),
    path('categoria/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/disabled/<int:id>', categoria_disabled, name='categoria_disabled'), # ajax

    
# rutas para administrar subcategorias.

    path('subcategoria/', SubcategoriaView.as_view(), name='subcategoria_list'),
    path('subcategoria/new', SubcategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategoria/edit/<int:pk>', SubcategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategoria/disabled/<int:id>', subcategoria_disabled, name='subcategoria_disabled'), # ajax

# rutas para administrar marca.

    path('marca/', MarcaView.as_view(), name='marca_list'),
    path('marca/new', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marca/disabled/<int:id>', marca_disabled, name='marca_disabled'), # ajax


# rutas para administrar Color.

    path('color/', ColorView.as_view(), name='color_list'),
    path('color/new', ColorNew.as_view(), name='color_new'),
    path('color/edit/<int:pk>', ColorEdit.as_view(), name='color_edit'),
    path('color/disabled/<int:id>', color_disabled, name='color_disabled'), # ajax

# rutas para administrar Productos.
    path('producto/', ProductoView.as_view(), name='producto_list'),
    path('producto/new', ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('producto/disabled/<int:id>', producto_disabled, name='producto_disabled'), # ajax


# rutas para administrar ciudad.

    path('ciudad/', CiudadView.as_view(), name='ciudad_list'),
    path('ciudad/new', CiudadNew.as_view(), name='ciudad_new'),
    path('ciudad/edit/<int:pk>', CiudadEdit.as_view(), name='ciudad_edit'),
    path('ciudad/disabled/<int:id>', ciudad_disabled, name='ciudad_disabled'), # ajax

# rutas para carrito

    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),


# rutas para administrar testimonios.

    path('testimonio/', TestimonioView.as_view(), name='testimonio_list'),
    path('testimonio/new', TestimonioNew.as_view(), name='testimonio_new'),
    path('testimonio/edit/<int:pk>', TestimonioEdit.as_view(), name='testimonio_edit'),
    path('testimonio/disabled/<int:id>', testimonio_disabled, name='testimonio_disabled'), # ajax


# rutas para guardar compra

    path('guardar_compra/', guardar_compra, name="guardar_compra"),




]