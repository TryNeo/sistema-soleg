sendingDataServerSide();

function sendingDataServerSide() {
    let url = 'http://127.0.0.1:8000/auth/login/';
    console.log(url);
    $('.form-horizontal').on('submit', function (e) {
        e.preventDefault();
            let formData = $(this).serializeArray();
            $.ajax({
                url: url,
                type: "POST",
                data: formData,
                dataType: 'json'
            }).done(function (data) {
                console.log(data.message)
            }).fail(function (data) {
                console.log(data['message'])
            })
    })
}