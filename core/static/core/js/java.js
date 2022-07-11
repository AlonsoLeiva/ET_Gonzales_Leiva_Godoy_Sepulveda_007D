

function MostrarMapa(){
    var b="Ocultar Mapa"
    var c="block"
    if(document.getElementById("boton1").value==b)
    {
        b="Ubicación de la tienda"
        c="none"
    }
    var i=document.getElementById("boton1").value=b;
    document.getElementById("mapas").style.display=c;

}

function MapaApi(){
    let watchId;
    let mapa = null;
    let mapaMarcador = null;	
    if (navigator.geolocation) {
	    watchId = navigator.geolocation.watchPosition(mostrarPosicion, mostrarErrores, opciones);	
    }else{
	    alert("Su navegador no es compatible con la geolocalización.");
    }

function mostrarPosicion(posicion) {
	let latitud = posicion.coords.latitude;
	let longitud = posicion.coords.longitude;
	let miPosicion = new google.maps.LatLng(latitud, longitud);

	
	let latitud2 = -33.511219;
	let longitud2 = -70.752550;
	let gdestino = new google.maps.LatLng(latitud2, longitud2);


	let objConfigDR={map:mapa}
	let objConfigDS={origin:miPosicion, destination:gdestino, travelMode:google.maps.TravelMode.DRIVING}
	let ds= new google.maps.DirectionsService();
	let dr= new google.maps.DirectionsRenderer(objConfigDR);
	ds.route(objConfigDS, fnRutear);

function fnRutear(resultados, status){
	if(status=='OK'){
		dr.setDirections(resultados);
	}else{
		alert('Error'+status);
	}
}

if (mapa == null) {
	let configuracion = {center: miPosicion, zoom: 16, mapTypeId: google.maps.MapTypeId.HYBRID};
	mapa = new google.maps.Map(document.getElementById("mapa"), configuracion);
//Marcador con la posicion actual
	mapaMarcador = new google.maps.Marker({position: miPosicion, title:"Esta es tu posición"});
	mapaMarcador.setMap(mapa);
}else{
	mapa.panTo(miPosicion);
	mapaMarcador.setPosition(miPosicion);
	}
}


function mostrarErrores(error) {
	switch (error.code) {
 		case error.PERMISSION_DENIED:
  			alert('Permiso denegado por el usuario.'); 
  			break;
   		case error.POSITION_UNAVAILABLE:
    		alert('La posición no se encuentra disponible.');
     		break; 
     	case error.TIMEOUT:
      		alert('Tiempo de espera agotado por el servidor.');
       		break;
        default:
         	alert('Error de Geolocalización desconocido :' + error.code);
	}
}

var opciones = {
	enableHighAccuracy: true,
	timeout: 10000,
	maximumAge: 1000
};

function detener() {
    navigator.geolocation.clearWatch(watchId);
    }
}


function MostrarTexto(){
    
    document.getElementById("texto").style.display="block";
	document.getElementById("texto2").style.display="block";
	document.getElementById("texto3").style.display="block";
}

function OcultarTexto(){
    document.getElementById("texto").style.display="none";
	document.getElementById("texto2").style.display="none";
	document.getElementById("texto3").style.display="none";
}