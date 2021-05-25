function login() {


    var mob_no = $('#mob_no').val();
    var password = $('#password').val();
    



    if ($("#mob_no").val() == "") {
        toastr.options = {
            positionClass: 'toast-top-center'
        };
        toastr.error("Please enter mobile number");
        var $notifyContainer = $('#toast-container').closest('.toast-top-center');
        if ($notifyContainer) {
            var windowHeight = $(window).height() - 50;
            $notifyContainer.css("margin-top", windowHeight / 2);
        }
        return false;
    }
    if ($("#password").val() == "") {
        toastr.options = {
            positionClass: 'toast-top-center'
        };
        toastr.error("Please enter password");
        var $notifyContainer = $('#toast-container').closest('.toast-top-center');
        if ($notifyContainer) {
            var windowHeight = $(window).height() - 50;
            $notifyContainer.css("margin-top", windowHeight / 2);
        }
        return false;
    }



    var csrf = window.CSRF_TOKEN
    $.ajax({
        type: 'post',
        url: '/technician/login-api',
        data: {
            "TECH_MOB": mob_no,
            "TECH_PASSWORD": password,
            'csrfmiddlewaretoken': csrf

        },
        success: function (data) {
            console.log(data.data)

            window.location.href = data.data.redirect_url

            localStorage.setItem('tech_id', data.data.id)

        },
        error: function (data) {
            window.location.href='/technician/index'
            console.log(data)
            if (data.status == 403) {
                toastr.options = {
                    positionClass: 'toast-top-center'
                };
                toastr.error("Please refresh your page!!!");
            } else {
                obj = JSON.parse(data.responseText)
                console.log(obj);

                console.log(obj.message);
                toastr.options = {
                    positionClass: 'toast-top-center'
                };
                toastr.error(obj.error);
            }
            var $notifyContainer = $('#toast-container').closest('.toast-top-center');
            if ($notifyContainer) {
                // align center
                var windowHeight = $(window).height() - 90;
                $notifyContainer.css("margin-top", windowHeight / 2);
            }

        },
    });
}
function logout(){

   $.ajax({
           type: 'post',
           url: '/logout',
           data: {
             'csrfmiddlewaretoken': window.CSRF_TOKEN // from index.html
           },
           success: function(data) {
             localStorage.clear();
             window.location.href = '/';
 //            location.reload();
           },
        error: function(data) {

                 obj = JSON.parse(data.responseText)
                  console.log(obj);
                  console.log(obj.message);
                  toastr.options = {
                     positionClass: 'toast-top-center'
                  };
                  toastr.error(obj.error);
                  var $notifyContainer = $('#toast-container').closest('.toast-top-center');
                     if ($notifyContainer) {
                        // align center
                        var windowHeight = $(window).height() - 90;
                        $notifyContainer.css("margin-top", windowHeight / 2);
                     }


         }
     });

 }