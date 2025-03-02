# Hay que importar esto para las respuestas
# Se añade Http404 para reconocer errores 404 y Redirección al final
from django.http import HttpResponse, HttpResponseRedirect
# Hay que añadir el objeto 404 de error y luego en
from django.shortcuts import render, get_object_or_404
# Con cmd + . nos crea un import de productos.form y ProductoForm
from productos.forms import ProductoForm
from .models import Producto  # Importamos nuestro modelo
# Create your views here.

# /productos (url de productos)

# VAmos a listar un conjunto de elementos mediante el método GET de de SQL


def index(request):  # todas las funciones de vista se llaman index
    productos = Producto.objects.all()
    return render(
        request,  # la funcion encargada de manejar nuestras peticiones y está arriba
        'index.html',  # el siguiente argumento es un string del nombre del archivo de la plantilla
        # hay que indicar los datos de la plantila. Y recibe un diccionario de productos
        context={'productos': productos}
    )


def detalle(request, producto_id):
    # Se puede utlizar pk (PrimaryKey)
    # Aquí llamamos al objeto de producto que sustitye el try and except
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )

# Parametros de URL
# def detalle(request, producto_id):
#     return HttpResponse(producto_id)

# Creamos una nueva funcion de formulario


def formulario(request):
    # Añadimos un if para ver si el método del formulario es POST guardar toda la información = formulario
    if request.method == 'POST':
        # Pasarle todo lo que esta en Post (los campos)
        form = ProductoForm(request.POST)
        if form.is_valid():  # Esto es para validar los datos.
            form.save()  # Si es valido lo guardamos y devolverlo a la url de productos.html
            return HttpResponseRedirect('/productos')
    else:  # Si no es una petición de Post, devuelve el formulario de nuevo.
        form = ProductoForm()  # **
    # creamos la instancia del formulario
    # form = ProductoForm()

    return render(
        request,
        'producto_form.html',  # esta es la plantilla que vamos a renderizar
        # pasamos un diccionario y el valor de la variable que acabamos de crear.
        # Asignamos la variable creada más arriba ** (ver asteriscos)
        {'form': form}
    )
