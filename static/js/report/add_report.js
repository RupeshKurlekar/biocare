$( document ).ready(function() {

})





    function checkReportForm(form)
    {



        if($('#patient').val() == "") {

            toastr.error("Please enter patient name");
            $("html").animate(
                {
                  scrollTop: $('#patient').offset().top-200
                },
                800
              );
            return false;
        }

        if($('#report_documents').val() == "") {

            toastr.error("Please select one report documents ");
            $("html").animate(
                {
                  scrollTop: $('#report_documents').offset().top-200
                },
                800
              );
            return false;
        }


        if($('#remark').val() == "") {

            toastr.error("Please enter remark");
            $("html").animate(
                {
                  scrollTop: $('#remark').offset().top-200
                },
                800
              );
            return false;
        }


    }




    $("#submitReport").click(function(){

        validation = checkReportForm();
        if (validation == false) {
            return false
        }
        // $('#submitExhibitorForm').prop('disabled', true);
        var patient       = $('#patient').val();
        var remark   = $('#remark').val();

        var csrfmiddlewaretoken     = $('#csrfmiddlewaretoken').val();

        var data= new FormData()

        data.append('PATIENT',patient)
        data.append('RP_REMARKS',remark)

        jQuery.each(jQuery('#report_documents')[0].files,function(i,file){
            data.append('RP_FILE',file)
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
            url: '/reports',
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
