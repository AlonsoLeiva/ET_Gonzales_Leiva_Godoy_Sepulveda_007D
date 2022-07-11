from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Donaciones, Personas, ProductoStock, Producto, Fundacion
from .forms import RegistroForm,  DonanteForm
from datetime import datetime

# Create your views here.
def home(request):

    return render(request, 'core/inicio.html')
    
def Quienes_Somos(request):
    return render (request, 'core/Quienes somos.html')

def registro(request):
    
    return render (request, 'core/Registro.html')

def donar(request):
    return render (request, 'core/donar.html')

def Galeriafotos(request):
    datos={

    }
    todos=ProductoStock.objects.all()
    datos['stock']=todos
    return render (request, 'core/Galeriadefotos.html',datos)

#Registrar Personas
def registrar_persona(request):
    datos={

    }
    nombre=request.POST['nombres']
    apellido=request.POST['apellido']
    rut=request.POST['rut']
    email=request.POST['email']
    contraseña=request.POST['contraseña']
    conficontraseña=request.POST['contraseña2']
    genero=request.POST['genero']
    estadocivil=request.POST['estadocivil']
    region=request.POST['region']
    direccion=request.POST['dirección']

    personaencontrada=Personas.objects.filter(rut=rut)
    if personaencontrada:
        datos['mensaje']= "Error, ya existe una persona registrada con ese Rut"
        return render(request, 'core/Registro_resultado.html',datos)
    else:
        datos['mensaje']= "Registro completado"
        persona=Personas.objects.create(nombre=nombre, apellido=apellido, rut=rut, email=email, contraseña=contraseña, conficontraseña=conficontraseña, genero=genero, estadocivil=estadocivil, region=region, direccion=direccion)
        return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Modificar Personas
def form_mod_registro(request,id):
    persona= Personas.objects.get(rut=id)
    try:
        rut=request.POST['rut']
    except:
        rut=0
    datos= {
        'Persona':persona
        
    }
    datos['rut']=rut
    return render(request, 'core/form_mod_registro.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Mandar para modificar
def editar_registro(request):
    nombre=request.POST['nombres']
    apellido=request.POST['apellido']
    rut=request.POST['rut']
    email=request.POST['email']
    contraseña=request.POST['contraseña']
    conficontraseña=request.POST['contraseña2']
    genero=request.POST['genero']
    estadocivil=request.POST['estadocivil']
    region=request.POST['region']
    direccion=request.POST['dirección']
    datos={

    }
    datos['mensaje'] = "Modificados correctamente"

    persona = Personas.objects.get(rut=rut)
    persona.nombre=nombre
    persona.apellido=apellido
    persona.email=email
    persona.contraseña=contraseña
    persona.conficontraseña=conficontraseña
    persona.genero=genero
    persona.estadocivil=estadocivil
    persona.region=region
    persona.direccion=direccion
    persona.save()

    return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Consulta de registro
def consultar_registro(request):
    datos={

    }
    try:
        rut=request.POST['rut']
        contraseña=request.POST['contraseña']
        personas=Personas.objects.filter(rut=rut).filter(contraseña=contraseña)
        personabuscada=Personas.objects.filter(rut=rut)
        #personabuscada=Personas.objects.filter(contraseña=contraseña)

        if personas:
                datos['mensaje']= "Usuario encontrado correctamente"
                personax=Personas.objects.get(rut=rut)
                datos['Persona']=personax
                return render (request, 'core/Consultar-registro.html',datos)
        elif personabuscada:
            datos['mensaje']= "Usuario encontrado pero contraseña incorrecta"
            return render (request, 'core/Consultar-registro.html',datos)    
        else:
            datos['mensaje'] = "Usuario no encontrado"
            return render (request, 'core/Consultar-registro.html',datos)
    except:
        datos['rut']=0
        return render (request, 'core/Consultar-registro.html',datos)
#---------------------------------------------------------------------------------------------------------------------
def consultar_datos(request):
    
    return render (request, 'core/Consultar-datos.html')

def registro_completo(request):
    return render (request, 'core/Registro_resultado.html')
#---------------------------------------------------------------------------------------------------------------------
#Registro de donante
def registrar_donante(request):
    datos={

    }
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    pago=request.POST['metodo']
    monto =request.POST['monto']
    tarjeta =request.POST['Numerotarjeta']
    fecha_expira =request.POST['fecha']
    cvv =request.POST['cvv']
    comentario=request.POST['comentario']
    todaspersonas=Donaciones.objects.all()
    cantpersonas=1
    for i in todaspersonas:
        cantpersonas=cantpersonas+1




    
    datos['cantidad']=cantpersonas

    datos['mensaje']= "Donacion completada"
    donante=Donaciones.objects.create(id=cantpersonas ,nombre=nombre, apellido=apellido, pago=pago, monto=monto, tarjeta=tarjeta, fecha_expira=fecha_expira, cvv=cvv, comentario=comentario)
    return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Pagina de modificacion
def form_mod_donacion(request,id):
    datos={

    }
    try:
        rut=request.POST['rut']
        donante = Donaciones.objects.get(id=id)
        datos['Donante']=donante
        datos['rut']=rut
        return render(request, 'core/form_mod_donar.html',datos)
    except:
        datos['rut']=0
        return render(request, 'core/form_mod_donar.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Mandar para modificar donaciones
def editar_donacion(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    pago=request.POST['metodo']
    monto =request.POST['monto']
    tarjeta =request.POST['Numerotarjeta']
    fecha_expira =request.POST['fecha']
    cvv =request.POST['cvv']
    comentario=request.POST['comentario']
    id=request.POST['id']
    datos={

    }
    datos['mensaje'] = "Modificados correctamente"

    donante = Donaciones.objects.get(id=id)
    donante.nombre=nombre
    donante.apellido=apellido
    donante.pago=pago
    donante.monto=monto
    donante.tarjeta=tarjeta
    donante.fecha_expira=fecha_expira
    donante.cvv=cvv
    donante.comentario=comentario
    donante.save()

    return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Pagina para consultar donaciones
def consultar_donacion(request):
    datos={

    }
    try:
        tarjeta=request.POST['tarjeta']
        donaciones=Donaciones.objects.filter(tarjeta=tarjeta)

        if donaciones:
            datos['mensaje']= "Donacion encontrada correctamente"
            donacionx=Donaciones.objects.filter(tarjeta=tarjeta)
            datos['Donacion']=donacionx
            return render (request, 'core/Consultar-registro-donar.html',datos)
        else:
            datos['mensaje'] = "Donación no encontrada"
            return render (request, 'core/Consultar-registro-donar.html',datos)
    except:
        datos['dona']=0
        return render (request, 'core/Consultar-registro-donar.html',datos)
#---------------------------------------------------------------------------------------------------------------------
def consultar_donar(request):
    
    return render (request, 'core/Consultar-datos-donar.html')

def consultar_ventas(request):
    
    return render (request, 'core/Consultar-ventas.html')

def ventas(request):
    datos={

    }
    datos['producto']=1
    return render (request, 'core/Ventas.html',datos)

def ventas_completado(request):
    datos={

        }
    try:    
        nombre=request.POST['nombre']
        datos['producto']=nombre

        return render (request, 'core/Ventas.html',datos)
    except:
        datos['producto']=0
        return render (request, 'core/Ventas.html',datos)


def ventas_procesar(request):
    datos={

    }
    try:
        rut=request.POST['rut']
        producto=request.POST['producto']
        cantidad=request.POST['cantidad']
        personas=Personas.objects.filter(rut=rut).filter(suscripcion='Si')
        productoencontrado=ProductoStock.objects.all()
        
        for i in productoencontrado:
                if i.nombreproducto==producto:
                    precio=int(i.precio)
                    precio2=int(i.precio)
                    precioinicio=int(i.precio)
    
        precio=precio*int(cantidad)
        precio2=precio2*int(cantidad)
        datos['precio']=precio
        datos['rut']=rut
        datos['producto']=producto
        datos['cantidad']=cantidad
        datos['precioinicio']=precioinicio
        descuento=0
        descuento2=0
        boleta=100000
        fecha=datetime.today().strftime('%Y-%m-%d')
        productos=Producto.objects.all()
        for i in productos:
            boleta=boleta+1
        datos['boleta']=boleta
        if personas:
            descuento=descuento+5
            descuento2=descuento2+5
        if precio>50000:
            descuento=descuento+10
            descuento2=descuento2+10
        if descuento==0:
            datos['descuento']=descuento
            datos['descuento2']=descuento2
            datos['fecha']=fecha
            precio=round(precio)
            datos['total']=precio
            return render (request, 'core/Ventas_procesar.html',datos)
        else:
            descuento=100-descuento
            descuento=descuento/100
            descuento2=descuento2/100
            precio=round(precio*descuento)
            datos['total']=precio
            datos['fecha']=fecha
            preciodescuento=round(precio2*descuento2)
            datos['descuento']=descuento
            datos['precio2']=preciodescuento
            datos['descuento2']=int(descuento2*100)
            
            return render (request, 'core/Ventas_procesar.html',datos)
    except:
        rut=0
        datos['rut']=rut
        return render (request, 'core/Ventas_procesar.html',datos)
    
    
def Consultar_compras(request,id):
    datos={

    }
    persona=Personas.objects.get(rut=id)
    try:
        compras=Producto.objects.filter(rut=id)
        rut=request.POST['rut']
        datos['mensaje']=0
    except:
        compras=1
        rut=0
    
    datos['compra']=compras
    datos['rut']=rut
    datos['persona']=persona
    
    return render (request, 'core/Consultar-compras.html',datos)

def consultar_boleta(request):
    datos={

    }
    encontrado=1
    try:
        boleta=request.POST['boleta']
        try:
            compras=Producto.objects.get(boleta=boleta)
        except:
            encontrado=0
            compras=0
    except:
        boleta=0
        compras=0
    
    datos['compra']=compras
    datos['mensaje']=1
    datos['boleta']=boleta
    datos['encontrado']=encontrado
    return render (request, 'core/Consultar-compras.html',datos)

def consultar_datos_compras(request):
    
    return render (request, 'core/Consultar-datos-compras.html')

def checkear_seguimiento(request):
    datos={

    }
    try:
        boleta=request.POST['boleta']
        compras=Producto.objects.get(boleta=boleta)
        try:
            rut=request.POST['rut']
            datos['rut']=rut
        except:
            rut=0
            datos['rut']=rut
    except:
        boleta=0
        compras=0
    datos['compra']=compras
    datos['mensaje']=1
    datos['boleta']=boleta
    return render (request, 'core/Consultar-seguimiento.html',datos)

def Iniciar_Sesion_Admin(request):
    
    return render (request, 'core/Consultar-datos-admin.html')

def form_mod_registro_admin(request,id):
    persona= Personas.objects.get(rut=id)
    try:
        rut=request.POST['rut']
    except:
        rut=0
    datos= {
        'Persona':persona
        
    }
    datos['rut']=rut
    return render(request, 'core/form_mod_registro_admin.html',datos)

def Consultar_registro_admin(request):
    datos={

    }
    try:
        usuario=request.POST['usuario']
        contraseña=request.POST['contraseña']
    except:
        usuario=0
        contraseña=0
        datos['usuario']=usuario
        datos['contraseña']=contraseña
    admin=Fundacion.objects.filter(usuario=usuario).filter(contraseña=contraseña)
    if admin:
        persona=Personas.objects.filter(suscripcion='Si')
        if persona:
            datos['Persona']=persona
        else:
            datos['Persona']=0
    else:
        datos['error']=1
    return render (request, 'core/Consultar-registro-admin.html',datos)

def eliminar_persona(request,id):
    datos={

    }
    persona = Personas.objects.get(rut=id)
    persona.delete()
    persona=Personas.objects.filter(suscripcion='Si')
    if persona:
        datos['Persona']=persona
    else:
        datos['Persona']=0

    return render (request, 'core/Consultar-registro-admin.html',datos)


    

    


   

