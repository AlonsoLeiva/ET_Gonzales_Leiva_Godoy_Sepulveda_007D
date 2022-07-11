from django import forms
from django.forms import ModelForm
from .models import Donaciones, Personas

# creamos nuestra clase para el formulario desde la base de datos

class RegistroForm(ModelForm):

    class Meta:
        model= Personas
        fields=['nombre','apellido','rut','email','contraseña','conficontraseña','genero','estadocivil','region','suscripcion','direccion']

class DonanteForm(ModelForm):

    class Meta:
        model= Donaciones
        fields=['id' ,'nombre','apellido', 'pago', 'monto', 'tarjeta', 'fecha_expira', 'cvv', 'comentario']

