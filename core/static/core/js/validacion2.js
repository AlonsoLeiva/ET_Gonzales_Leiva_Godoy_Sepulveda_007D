		$().ready(function() {

			$.validator.addMethod("formtarjeta", function (value, element) {
                var patron = /^(?:(4[0-9]{12}(?:[0-9]{3})?)|(5[1-5][0-9]{14})|(6(?:011|5[0-9]{2})[0-9]{12})|(3[47][0-9]{13})|(3(?:0[0-5]|[68][0-9])[0-9]{11})|((?:2131|1800|35[0-9]{3})[0-9]{11}))$/;
                return this.optional(element) || patron.test(value);
             }, "Formato del tarjeta incorrecto");

			$("#formulario-donar").validate({
				rules: {
					nombre: {
						required: true,
						minlength: 3,
					},
					apellido: {
						required: true,
						minlength: 3
					},
					pago: {
						required: true,
					},
					tarjeta: {
						formtarjeta : true,
						required: true,
						minlength:16
					},
					fecha_expira: {
						required: true
					},
					monto: {
						required: true,
						number: true,
						minlength:4
					},
					cvv: {
						required: true,
						minlength:3,
						maxlength:3
					},
					aceptar: {
						required: true
					},

					monto: {
						required: true,
						minlength:4,
						maxlength:7		
					},
				},
				messages: {
					nombre: {
						required: "Debes de ingresar un nombre",
						minlength: "Tu nombre debe tener al menos 3 caracteres"
					},
					apellido: {
						required: "Debes ingresar un apellido",
						minlength: "Tu Apellido debe tener al menos 3 caracteres"
					},
					pago: {required: "Debes ingresar un tipo de pago"
					},
					tarjeta: {
						formtarjeta: "Debes ingresar el numero de tu tarjeta valido",
						required: "Debes ingresar el numero de tu tarjeta valido",
						minlength: "Faltan digitos de su tarjeta"
					},
					monto: {
						number: "El monto debe ser númerico",
						required: "Debes ingresar un monto a donar",
						minlength: "El minimo de donativos es de $1000 pesos"
					},
					fecha_expira: {
						required: "Debes ingresar la fecha de expiracion"
					},
					cvv: {
						required: "Debes ingresar los 3 digitos de la parte trasera de tu tarjeta",
						minlength: "Faltan digitos de su CVV",
						maxlength: "Sobrepasaste la cantidad de digitos de tu CVV"
					},
					aceptar: {
						required: "Debes aceptar la politica no reembolsable"
						
					}
				}

			});
		});

		