from django.urls import path
# from . significa "la carpeta donde yo me encuentro" queremos ese archivo importado
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),  # dejamos un string vacio
    # Creamos una ruta nueva dentro de productos.
    path('formulario', views.formulario, name='formulario'),
    path(
        # Aquí definimos un numero entero para especificar el tipo de dato esperado
        '<int:producto_id>',
        views.detalle,
        name='detalle'
    ),  # dejamos un string vacio
]
