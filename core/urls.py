from django.urls import path
from .views import consultar_datos, home,donar,Galeriafotos,registro,Quienes_Somos,registrar_persona,form_mod_registro,editar_registro,consultar_registro,consultar_datos, registrar_donante, form_mod_donacion, editar_donacion,consultar_donar,consultar_donacion,consultar_ventas,ventas,ventas_procesar,Consultar_compras,consultar_boleta,consultar_datos_compras,checkear_seguimiento,ventas_completado,Iniciar_Sesion_Admin,Consultar_registro_admin,form_mod_registro_admin,eliminar_persona


urlpatterns = [
    path ('', home,name="home"), 
    path ('QuienesSomos', Quienes_Somos,name="QuienesSomos"),
    path ('form-registro', registro,name="form-registro"),
    path ('Galeria', Galeriafotos,name="Galeria"),
    path ('registrarPersona/', registrar_persona),
    path ('form-mod-registro/<id>', form_mod_registro, name="form_mod_registro"),
    path ('Editar-registro/', editar_registro, name="Editar_registro"),
    path ('Consultar-datos', consultar_datos, name="Consultar_datos"),
    path ('Consultar-registro/', consultar_registro, name="Consultar_registro"),
    path ('form-donar', donar, name="form-donar"),
    path ('registrar_donante/', registrar_donante),
    path ('form-mod-donar/<id>', form_mod_donacion, name="form_mod_donacion"),
    path ('editar-donacion/', editar_donacion, name="editar_donacion"),
    path ('Consultar-donar', consultar_donar, name="Consultar_datos_donar"),
    path ('Consultar-donacion/', consultar_donacion, name="Consultar_donacion"),
    path ('Consultar_ventas', consultar_ventas, name="Consultar_ventas"),
    path ('Ventas', ventas, name="Ventas"),
    path ('Ventas_completado', ventas_completado, name="Ventas_completado"),
    path ('Compra_resultado', ventas, name="Compra_resultado"),
    path ('ventas_procesar/', ventas_procesar, name="ventas_procesar"),
    path ('Consultar_compras/<id>', Consultar_compras, name="Consultar_compras"),
    path ('Datos_boleta/', consultar_boleta, name="Datos_boleta"),
    path ('Consultar_boleta', consultar_datos_compras, name="Consultar_boleta"),
    path ('Consultar_seguimiento', checkear_seguimiento, name="Consultar_seguimiento"),
    path ('Iniciar_Sesion', Iniciar_Sesion_Admin, name="Iniciar_Sesion"),
    path ('Registro-admin', Consultar_registro_admin, name="Registro-admin"),
    path ('form-mod-registro-admin/<id>', form_mod_registro_admin, name="form-mod-registro-admin"),
    path ('eliminar_persona/<id>', eliminar_persona, name="eliminar_persona"),
]

