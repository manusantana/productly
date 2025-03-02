# Importamos desde donde estamos "." los modelos
from . import models
# Importamos el model de formularios
from django.forms import ModelForm

# Creamos una clase igual que el modelo de ProductoForm extiende de ModelForm.


class ProductoForm(ModelForm):
    # A su vez tenemos que agregar otra clase que se llama Meta
    class Meta:
        # Especificar que el modelo viene de productos
        model = models.Producto
        # Aquí metemos una lista con los campos que queremos que tenga el formulario
        fields = ['nombre', 'stock', 'puntuacion', 'categoria']
