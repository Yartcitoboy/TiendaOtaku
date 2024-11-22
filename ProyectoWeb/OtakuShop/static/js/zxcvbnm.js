$(document).ready(function () {
    $("#contact_form")
      .bootstrapValidator({
        //  ESTO NO LE PRESTE MUCHA ATENCION ES PARA VALIDAR EN EL FORM(PERSONALIZADO) POR ALGUA RAZON NO FUNCIONA XD
        feedbackIcons: {
          valid: "glyphicon glyphicon-ok",
          invalid: "glyphicon glyphicon-remove",
          validating: "glyphicon glyphicon-refresh",
        },
        fields: {
          nombre: {
            validators: {
              stringLength: {
                Request: true,
                min: 2,
              },
              notEmpty: {
                message: "Por favor proporcione su nombre",
              },
            },
          },
          run: {
            validators: {
              stringLength: {
                min: 8,
              },
              notEmpty: {
                message: "Por favor proporcione su run",
              },
            },
          },
          email: {
            validators: {
              stringLength: {
                min: 8,
              },
              notEmpty: {
                message: "Por favor proporcione su run",
              },
            },
          },
          fono: {
            validators: {
              notEmpty: {
                message: "Por favor proporcione su telefono",
              },
              stringLength: {
                min: 9,
                max: 9,
                message: "El número de teléfono debe tener exactamente 9 dígitos.",
              },
              regexp: {
                regexp: /^[0-9]+$/,
                message: "Ingrese solo números para el teléfono.",
              },
            },
          },
          contraseña: {
            validators: {
              stringLength: {
                min: 6,
              },
              notEmpty: {
                message: "Por favor proporcione su Contraseña",
              },
            },
          },
        },
      })
      .on("success.form.bv", function (e) {
        $("#success_message").slideDown({ opacity: "show" }, "slow"); 
        $("#contact_form").data("bootstrapValidator").resetForm();
  
  
        e.preventDefault();
  
  
        var $form = $(e.target);
  
  
        var bv = $form.data("bootstrapValidator");
  
  
        $.post(
          $form.attr("action"),
          $form.serialize(),
          function (result) {
            console.log(result);
          },
          "json"
        );
      });
  });



$(document).ready(function () {
    $("#run").on("input", function () {
        let value = this.value.replace(/[^0-9kK]/g, ""); 
        if (value.includes("-")) {
            let parts = value.split("-");
            value = parts[0]; 
        }
        if (value.length > 8) {
            value = value.slice(0, 8); 
        }
        if (value.length === 8) {
            const dv = calcularDV(value);
            this.value = value; 
        }
    });

    $("#run").on("blur", function () {
        let value = this.value.replace(/[^0-9kK]/g, ""); 

        if (value.length === 8) {
            const dv = calcularDV(value);
            this.value = `${value}-${dv}`; 
        }
    });

    const calcularDV = (rut) => {
        let suma = 0;
        let multiplicador = 2;
        for (let i = rut.length - 1; i >= 0; i--) {
            suma += parseInt(rut[i]) * multiplicador;
            multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
        }
        const resto = 11 - (suma % 11);
        if (resto === 11) {
            return '0';
        } else if (resto === 10) {
            return 'K';
        } else {
            return resto.toString();
        }
    };
});

  