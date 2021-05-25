$( document ).ready(function() {

})


function IsEmail(email) {
    // var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    var regex = /^[a-zA-Z0-9]([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    // var regex = /^[a-zA-Z0-9]([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if(!regex.test(email)) {
        return false;
    }else{
        return true;
    }
}
function isMobileValid(number) {
    console
    if(number.length >=9 && number.length  <=12) {
        return true;
    }else{
        return false;
    }
}





    function checkTechnicianForm(form)
    {



        if($('#full_name').val() == "") {

            toastr.error("Please enter full name");
            $("html").animate(
                {
                  scrollTop: $('#full_name').offset().top-200
                },
                800
              );
            return false;
        }

        if($('#email').val() == "") {

            toastr.error("Please enter email");
            $("html").animate(
                {
                  scrollTop: $('#email').offset().top-200
                },
                800
              );
            return false;
        }
        if(IsEmail($('#email').val())==false){

            toastr.error("Invalid email");
            $("html").animate(
                {
                  scrollTop: $('#email').offset().top-200
                },
                800
              );
            return false;
        }
        if($('#mobile_no').val() == "") {

            toastr.error("Please enter mobile number");
            $("html").animate(
                {
                  scrollTop: $('#mobile_no').offset().top-200
                },
                800
              );
            return false;
        }


        if($('#mobile_no').val() !== ""  &&  isMobileValid($('#mobile_no').val())==false){
            toastr.error("Invalid mobile number");
            $("html").animate(
                {
                  scrollTop: $('#mobile_no').offset().top-200
                },
                800
              );
            return false;
        }

        if($('#address').val() == "") {

            toastr.error("Please enter address");
            $("html").animate(
                {
                  scrollTop: $('#address').offset().top-200
                },
                800
              );
            return false;
        }
        if($('#password').val() == "") {

            toastr.error("Please enter address");
            $("html").animate(
                {
                  scrollTop: $('#address').offset().top-200
                },
                800
              );
            return false;
        }
        if($('#profile_picture').val() == "") {

            toastr.error("Please select one image ");
            $("html").animate(
                {
                  scrollTop: $('#profile_picture').offset().top-200
                },
                800
              );
            return false;
        }




    }

$("#mobile_no").on("keypress keyup blur",function (event) {
        $(this).val($(this).val().replace(/[^\d].+/, ""));
        if ((event.which < 48 || event.which > 57)) {
            event.preventDefault();
        }
    });

$('#full_name').on('keypress', function (event) {
        var regex = new RegExp("^[a-zA-Z \b]+$");
        var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
        if (!regex.test(key)) {
           event.preventDefault();
           return false;
        }
    });


    $("#submitTechnician").click(function(){

        validation = checkTechnicianForm();
        if (validation == false) {
            return false
        }
        // $('#submitExhibitorForm').prop('disabled', true);
        var email       = $('#email').val();
        var full_name   = $('#full_name').val();
        var mobile_no   = $('#mobile_no').val();
        var address     = $('#address').val();
        var password     = $('#password').val();
        var csrfmiddlewaretoken     = $('#csrfmiddlewaretoken').val();



        var data= new FormData()

        data.append('TECH_NAME',full_name)
        data.append('TECH_MOB',mobile_no)
        data.append('TECH_EMAIL',email)
        data.append('TECH_PASSWORD',password)
        data.append('TECH_ADDRESS',address)

        jQuery.each(jQuery('#profile_picture')[0].files,function(i,file){
            data.append('TECH_IMG',file)
        })
        data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
        console.log('daaaa',data)
        swal({
            title: 'Please Wait',
            allowEscapeKey: false,
            allowOutsideClick: false,
            showLoaderOnConfirm: true,
            buttons: false

          })
        $.ajax({
            type: 'post',
            url: '/technicians',
            data:data,
            processData: false,
            contentType: false,

            success: function(data) {
                swal.close()
                 toastr.success("Your application is submitted successfully for the admin approval and once admin has approved the application you will get the confirmation email on your registered email ID")
                },
              error: function(data) {
                console.log(data)
                swal.close()
                if (data.status == 403) {
                toastr.options = {
                    positionClass: 'toast-top-center'
                };
                toastr.error("Please refresh your page!!!");
            }
            else{

                   obj = JSON.parse(data.responseText)
                   console.log(obj);
                   console.log(obj.message);
                   if (obj.error){
                    toastr.error(obj.error);
                   }
                   else{
                    toastr.error(obj.message);

                   }
              }
              }
          });
    })
