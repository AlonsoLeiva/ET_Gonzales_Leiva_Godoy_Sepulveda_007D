from django.contrib import admin
from .models import Donaciones, Personas, Producto, ProductoStock, Fundacion

# Register your models here.
# Permite administrar el modelo completo


admin.site.register(Personas)
admin.site.register(Donaciones)
admin.site.register(Producto)
admin.site.register(ProductoStock)
admin.site.register(Fundacion)