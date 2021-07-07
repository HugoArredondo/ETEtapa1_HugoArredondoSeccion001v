$(function() 
      {
        $("#form-reg").validate({
            rules: {
                    iden: "required",
                    photo: "required",
                    nom: "required",
                    phone: "required",
                    adress: "required",
                    email: {
                        required: true,
                        email: true
                    },
                    pais: "required",
                    password: "required",
                    money: "required"  
                    
            }, //rules
            messages: {
                iden: {
                    required: 'Ingresa número de identificación'
                },
                photo: {
                    required: 'Carga una foto'
                },
                nom: {
                    required: 'Ingresa tu nombre completo'
                },
                phone:{
                    required: 'Ingrese un número de contacto'
                },
                adress: {
                    required: 'Ingresa una dirección'
                },
                email: {
                    required: 'Ingresa tu correo electrónico',
                    email: 'Formato de correo no válido'
                },
                pais: {
                    required: 'Ingresa un País'
                },
                password: {
                    required: 'Ingresa una contraseña',
                    minlength: 'Caracteres insuficientes'
                },
                money: {
                    required: 'Ingresa una moneda'
                }
            }//messages
        }); //$('formulario').validate
    }); //function