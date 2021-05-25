$( document ).ready(function() {




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





    function checkPatientForm(form)
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
        if($('#gender').val() == "") {

            toastr.error("Please select gender");
            $("html").animate(
                {
                  scrollTop: $('#gender').offset().top-200
                },
                800
              );
            return false;
        }
        if($('#age').val() == "") {

            toastr.error("Please enter age");
            $("html").animate(
                {
                  scrollTop: $('#age').offset().top-200
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


    $("#submitPatient").click(function(){

        validation = checkPatientForm();
        if (validation == false) {
            return false
        }
        // $('#submitExhibitorForm').prop('disabled', true);

        var full_name   = $('#full_name').val();
        var gender     = $('#gender').val();
        var age     = $('#age').val();
        var mobile_no   = $('#mobile_no').val();
        var csrfmiddlewaretoken     = $('#csrfmiddlewaretoken').val();



        var data= new FormData()

        data.append('PT_NAME',full_name)
        data.append('PT_GENDER',gender)
        data.append('PT_AGE',age)
        data.append('PT_MOB',mobile_no)



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
            url: '/patients',
            data:data,
            processData: false,
            contentType: false,

            success: function(data) {
                swal.close()
                 toastr.success("Your application is submitted successfully")
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
