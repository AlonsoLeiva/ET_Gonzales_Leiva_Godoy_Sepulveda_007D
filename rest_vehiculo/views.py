from ast import If
from asyncio.windows_events import NULL
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Personas, Donaciones, ProductoStock, Producto
from .serializers import PersonaSerializer, DonacionesSerializer, ProductoSerializer
@csrf_exempt
@api_view(['GET','POST'])
def lista_personas(request):
    """
    Lista de todos las personas
    """
    if request.method == 'GET':
        persona = Personas.objects.all()
        serializer = PersonaSerializer(persona, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = PersonaSerializer(data=request.data)
        rut=request.POST['rut']
        personaencontrada=Personas.objects.filter(rut=rut)
        datos={

        }
        if serializer.is_valid():
            if personaencontrada:
                datos['mensaje']= "Error, ya existe una persona registrada con ese Rut"
                return render(request, 'core/Registro_resultado.html',datos)
            else:
                datos['mensaje']= "Registro completado"
                serializer.save()
                return render(request, 'core/Registro_resultado.html',datos)
        else:
            datos['mensaje']= "Error, ya existe una persona registrada con ese Rut"
            return render(request, 'core/Registro_resultado.html',datos)

#============================================================================================
@csrf_exempt
@api_view(['GET','POST'])
def lista_donaciones(request):
    """
    Lista de todos las donaciones
    """
    if request.method == 'GET':
        donaciones = Donaciones.objects.all()
        serializer = DonacionesSerializer(donaciones, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = DonacionesSerializer(data=request.data)
        datos ={

        }
        if serializer.is_valid():
            serializer.save()
            datos['mensaje']= "Donación completada"
            return render(request, 'core/Registro_resultado.html',datos)
        else:
            datos['mensaje']= "Se ha producido un error inesperado, la donación no se pudo efectuar"
            return render(request, 'core/Registro_resultado.html',datos)

#============================================================================================

@api_view(['GET','PUT','DELETE','POST'])
def detalle_personas(request,id):
    """
    Get, Update, o delete de una persona en particular
    """
    persona = Personas.objects.get(rut=id)
    try:
        persona = Personas.objects.get(rut=id)
    except Personas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            datos={
            }
            datos['mensaje'] = "Modificados correctamente"
            serializer.save()
            return render(request, 'core/Registro_resultado.html',datos)
        else:
            datos={
            }
            datos['mensaje'] = "Hubo un error inesperado, no se pudieron modificar los datos"
            return render(request, 'core/Registro_resultado.html',datos)
    elif request.method == 'DELETE':
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#============================================================================================
@api_view(['GET','PUT','DELETE','POST'])
def detalle_donaciones(request,id):
    """
    Get, Update, o delete de una donacion en particular
    """
    try:
        donacion = Donaciones.objects.get(id=id)
    except Donaciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DonacionesSerializer(donacion)
        return Response(serializer.data)
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = DonacionesSerializer(donacion, data=request.data)
        if serializer.is_valid():
            datos={
            }
            datos['mensaje'] = "Modificados correctamente"
            serializer.save()
            return render(request, 'core/Registro_resultado.html',datos)
        else:
            datos={
            }
            datos['mensaje'] = "Hubo un error inesperado, no se pudieron modificar los datos"
            return render(request, 'core/Registro_resultado.html',datos)
    elif request.method == 'DELETE':
        donacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#============================================================================================
@api_view(['GET','POST'])
def lista_productos(request):
    """
    Lista de todos los productos
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=request.data)
        productostotales=ProductoStock.objects.all()
        nombre=request.POST['producto']
        cantidad=int(request.POST['cantidad'])
        for ve in productostotales:
            if ve.nombreproducto==nombre:
                stockdisponible=ve.stock
        
        datos={

            }
        datos['boleta']=0
        if serializer.is_valid():
            if cantidad>stockdisponible:
                datos['mensaje']= "Error, la cantidad que desea comprar supera al stock disponible. Puede ver nuestro stock en la lista de productos"
                return render(request, 'core/Compra_resultado.html',datos)
            else:
                datos['mensaje']= "Compra completada"
                boleta=request.POST['boleta']
                datos['boleta']=boleta
                productodescontar = ProductoStock.objects.get(nombreproducto=nombre)
                productodescontar.stock=productodescontar.stock-cantidad
                productodescontar.save()
                serializer.save()
                return render(request, 'core/Compra_resultado.html',datos)
        else:
            datos['mensaje']= "Se ha producido un error inesperado, la compra no se pudo efectuar"
            datos['boleta']=0
            return render(request, 'core/Compra_resultado.html',datos)