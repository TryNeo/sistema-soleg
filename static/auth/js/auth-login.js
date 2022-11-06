$(document).ready(function() {
    const fieldsToValidate = ['username','password']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
        invalidFeedBackClass: 'invalid-tooltip',
    });

    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=username]')){
            let value= $(el).val()
            if (!validateEmptyField(value)){
                return 'El correo electrónico es obligatorio';
            }

            if (!validaEmail(value)){
                return 'El correo electrónico '+value +' ingresado no es valido';
            }
        }

        if($(el).is('[name=password]')){
            let value= $(el).val()
            
            if (!validateEmptyField(value)){
                return 'La contraseña es obligatorio';
            }

            if (!validateUser(value)){
                return 'La contraseña ingresada no es valida';
            }

        }
    }

    sendingDataLogin(validatorServerSide,fieldsToValidate)
});



function sendingDataLogin(validatorServerSide,fieldsToValidate){
    $('#id_remember_me').on('change', function(){ 
        $('#id_remember_me').removeClass('is-valid');
        this.value = this.checked ? 1 : 0;
    }).change();
    
    $('#fntLogin').on('submit', function (e) {
        e.preventDefault();
        if(validatorServerSide.checkAll('.needs-validation') === 0){
            let formData = $(this).serializeArray();
            $.ajax({
                url:   $('#fntLogin').attr("action"),
                type:  $('#fntLogin').attr("method"),
                data:  formData,
                dataType: 'json'
            }).done(function (data) {
                console.log('aqui')
            }).fail(function (data) {
                fieldsToValidate.forEach((value,index) => {
                    if (data.responseJSON['message'].hasOwnProperty(fieldsToValidate[index])){
                        validatorServerSide.errorTrigger($('[name='+fieldsToValidate[index]+']'), data.responseJSON['message'][''+fieldsToValidate[index]+'']);
                    }
                });
            })
        }else{
            $('#id_remember_me').removeClass('is-valid');
        }
    })
}