from tabnanny import verbose
from django.db import models

# Create your models here.




class Personas(models.Model):
    nombre=models.CharField(max_length=100,verbose_name='Nombres')
    apellido=models.CharField(max_length=100,verbose_name='Apellidos')
    rut=models.CharField(max_length=100,primary_key=True,verbose_name='Rut')
    email=models.CharField(max_length=200,verbose_name='Email')
    contraseña=models.CharField(max_length=100,verbose_name='Contraseña')
    conficontraseña=models.CharField(max_length=100,verbose_name='Confirmar Contraseña')
    genero=models.CharField(max_length=100,verbose_name='Género')
    estadocivil=models.CharField(max_length=100,verbose_name='Estado Civil')
    region=models.CharField(max_length=100,verbose_name='Region')
    suscripcion=models.CharField(max_length=100,verbose_name='Suscripción')
    direccion=models.CharField(max_length=100,verbose_name='Dirección')

    def __str__(self):
        return self.rut

    
class Donaciones(models.Model):
    nombre=models.CharField(max_length=100,verbose_name='Nombres')
    apellido=models.CharField(max_length=100,verbose_name='Apellidos')
    pago=models.CharField(max_length=100,verbose_name='Pago')
    monto=models.CharField(max_length=200,verbose_name='Monto')
    tarjeta=models.CharField(max_length=100, verbose_name='Tarjeta')
    fecha_expira=models.CharField(max_length=100,verbose_name='Fecha de expiracion')
    cvv=models.CharField(max_length=100,verbose_name='CVV')
    comentario=models.CharField(max_length=100,blank=True,verbose_name='Comentario')

    def __str__(self):
        return self.apellido

class Producto(models.Model):
    boleta=models.IntegerField(primary_key=True,verbose_name='Boleta')
    fecha_efectuada=models.CharField(max_length=100,verbose_name='Fecha Efectuada')
    producto=models.CharField(max_length=100,verbose_name='Producto')
    cantidad=models.IntegerField(verbose_name='Cantidad de Productos')
    rut=models.CharField(max_length=100,verbose_name='Rut')
    email=models.CharField(max_length=100,verbose_name='Email')
    metodo=models.CharField(max_length=100,verbose_name='Metodo de pago')
    tarjeta=models.CharField(max_length=100,verbose_name='Tarjeta')
    fecha=models.CharField(max_length=100,verbose_name='Fecha de expiración')
    cvv=models.IntegerField(verbose_name='CVV')
    direccion=models.CharField(max_length=100,verbose_name='Dirección')
    total=models.IntegerField(verbose_name='Total de Boleta')

    def __str__(self):
        return self.rut

class ProductoStock(models.Model):
    id=models.CharField(primary_key=True ,max_length=100,verbose_name='Id Producto')
    nombreproducto=models.CharField(max_length=100,verbose_name='Nombre Producto')
    stock=models.IntegerField(verbose_name='Stock')
    precio=models.IntegerField(verbose_name='Precio')
    
    def __str__(self):
        return self.nombreproducto

class Fundacion(models.Model):
    usuario=models.CharField(max_length=100,verbose_name='Nombre de Usuario')
    contraseña=models.CharField(max_length=100,verbose_name='Contraseña')

    def __str__(self):
        return self.usuario