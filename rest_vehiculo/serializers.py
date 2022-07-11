from rest_framework import serializers
from core.models import Personas, Donaciones, Producto

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['nombre','apellido','rut','email','contraseña','conficontraseña','genero','estadocivil','region','suscripcion','direccion']

class DonacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donaciones
        fields = ['nombre','apellido','pago','monto','tarjeta','fecha_expira','cvv','comentario']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['boleta' ,'fecha_efectuada' ,'producto','cantidad','rut','email','metodo','tarjeta','fecha','cvv','direccion','total']
