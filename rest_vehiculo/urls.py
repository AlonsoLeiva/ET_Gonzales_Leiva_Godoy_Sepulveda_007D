from django.urls import path
from rest_vehiculo.views import lista_personas, lista_donaciones, detalle_personas, lista_productos, detalle_donaciones

urlpatterns = [
    path('lista_personas/', lista_personas, name="lista_personas"),
    path('lista_donaciones/', lista_donaciones, name="lista_donaciones"),
    path('detalle_personas/<id>', detalle_personas, name="detalle_personas"),
    path('lista_productos/', lista_productos, name="lista_productos"),
    path('detalle_donaciones/<id>', detalle_donaciones, name="detalle_donaciones"),
]