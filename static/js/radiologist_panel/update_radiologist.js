
$(document).ready(function () {
    window.rdlg_id = localStorage.getItem('rdlg_id')

    $.ajax({
        type: 'get',
        url: '/radiologist_details/'+rdlg_id,
        data: {

        },
        success: function (data) {
            console.log(data.data)
            var radiologist = data.data;
            if (radiologist) {
                $('#full_name').val(radiologist.RDLG_NAME)
                $('#email').val(radiologist.RDLG_EMAIL);
                $('#mobile_no').val(radiologist.RDLG_MOB_NO);
                $('#address').text(radiologist.RDLG_ADDRESS);
                $('#profile_image').attr('src',radiologist.RDLG_IMG);
                $('#qualification').val(radiologist.RDLG_QUALIFICATION);
                $('#experience').val(radiologist.RDLG_EXPERIENCE);
                $('#speciality').val(radiologist.RDLG_SPECIALITY);
                $('#radiologist_area').val(radiologist.RDLG_AREA);
            }
           

        },
        error: function (data) {

            console.log('err', data);
            obj = JSON.parse(data.responseText)
            console.log(obj.message);
            toastr.error(obj.error);
        }
    })
})


function IsEmail(email) {
    // var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    var regex = /^(?!\_)(?!_*_$)([0-9A-Za-z]+\.)*[a-zA-Z0-9_+-]+@([\w+-]+\.)*[\w+-]+\.[a-zA-Z]{2,4}$/;
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





    function checkRadiologistForm(form)
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
        if($('#qualification').val() == "") {

            toastr.error("Please enter qualification");
            $("html").animate(
                {
                  scrollTop: $('#qualification').offset().top-200
                },
                800
              );
            return false;
        }
        if($('#experience').val() == "") {

            toastr.error("Please enter experience");
            $("html").animate(
                {
                  scrollTop: $('#experience').offset().top-200
                },
                800
              );
            return false;
        }
        if($('#radiologist_area').val() == "") {

            toastr.error("Please enter area");
            $("html").animate(
                {
                  scrollTop: $('#area').offset().top-200
                },
                800
              );
            return false;
        }
        if($('#speciality').val() == "") {

            toastr.error("Please enter speciality");
            $("html").animate(
                {
                  scrollTop: $('#speciality').offset().top-200
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

    function updateRadiologist(){

        validation = checkRadiologistForm();
        if (validation == false) {
            return false
        }
        // $('#submitExhibitorForm').prop('disabled', true);
        var csrf = window.CSRF_TOKEN


        var full_name =    $('#full_name').val()
        var email =    $('#email').val();
        var mobile_no =    $('#mobile_no').val();
        var address =    $('#address').val();
        var qualification =    $('#qualification').val();
        var experience =    $('#experience').val();
        var speciality =    $('#speciality').val();
        var area =    $('#radiologist_area').val();
        var csrfmiddlewaretoken     =csrf



        var data= new FormData()

        data.append('RDLG_NAME',full_name)
        data.append('RDLG_MOB_NO',mobile_no)
        data.append('RDLG_EMAIL',email)
        data.append('RDLG_ADDRESS',address)
        data.append('RDLG_QUALIFICATION',qualification)
        data.append('RDLG_EXPERIENCE',experience)
        data.append('RDLG_SPECIALITY',speciality)
        data.append('RDLG_AREA',area)
        if($('#profile_picture').val()){
            jQuery.each(jQuery('#profile_picture')[0].files,function(i,file){
                data.append('RDLG_IMG',file)
            })
        }
        else{
            data.append('RDLG_IMG',"")

        }
        
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
            url: '/radiologist_update/'+window.rdlg_id,
            data:data,
            processData: false,
            contentType: false,

            success: function(data) {
                swal.close()
                 swal("Successful", "Radiologist updated successfully", "success").then(function() {
                  location.reload()
                });
              
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
    }
