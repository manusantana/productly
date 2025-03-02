# Hay que importar esto para las respuestas
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto  # Importamos nuestro modelo
# Create your views here.

# /productos (url de productos)

# VAmos a listar un conjunto de elementos mediante el método GET de de SQL


def index(request):  # todas las funciones de vista se llaman index
    productos = Producto.objects.all().values()

    # Devuelve el primer elemento y el nombre
    return JsonResponse(list(productos), safe=False)
    # productos = Producto.objects.all() #All nos permite buscar todo lo que esté en la bbdd
    # productos = Producto.objects.filter(puntuacion__gte=3) #Nos permite filtrar por algun atributo, puntaje, codigos, etc... gte(mayor/igual)
    # productos = Producto.objects.filter(puntuacion__lte=3) #menor/igual que
    # productos = Producto.objects.filter(puntuacion__lt=3) #menor que
    # productos = Producto.objects.filter(puntuacion__gt=3) #mayor que
    # productos = Producto.objects.filter(puntuacion=3) #igual que 3
    # productos = Producto.objects.get(id=1) #Me traigo un producto con el id 1
    # productos = Producto.objects.get(id=1) #Me traigo un producto PrimaryKey 1
