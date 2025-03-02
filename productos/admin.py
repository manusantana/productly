from django.contrib import admin
# Importamos el archivo de los modelos y cuales son los modelos que queremos importar.
from .models import Categoria, Producto
# En este caso categoria y Producto.

# Para personalizar el panel tenemos que crear una nueva clase para representar lo que queremos mostar


class CategoriaAdmin(admin.ModelAdmin):
    # A través de tupla configuramos como queremos que se vea según los campos creados
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    # Aquí tenemos que añadir un espacio después de la ,
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.


# Llamamos a un método para que a través de las clases llame a los modelos
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
