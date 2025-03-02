from django.db import models
# Para importar el huso horario para que genere el registro de fecha de creacion de producto
from django.utils import timezone
# Create your models here.


class Categoria(models.Model):
    # Así es como llamamos a un string en el ORM de Django y definimos una longitud máxima.
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    # string con un max de caracteres
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    stock = models.IntegerField()  # numero entero
    puntuacion = models.FloatField()  # numeros decimales
    # Alternativas cuando asignamos una ForeignKey entre campos:
    # CASCADE = elimina el producto si se elmina la categoría.
    # PROTECT = Da un error si queremos eliminar la categoría.
    # RESTRICT = Deja eliminar la categoría cuando no existan productos.
    # SET_NULL = actualiza a valor Nulo en la categoría. Categoría =Null
    # SET_DEFAULT = asigna un valor por defecto

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    # Se le asigna una fecha de creación automática
    creado_en = models.DateTimeField(default=timezone.now)
