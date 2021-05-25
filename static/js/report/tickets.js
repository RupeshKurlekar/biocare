$( document ).ready(function() {


})


    function checkTicketForm(form)
    {



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



    $("#submitTicket").click(function(){

        validation = checkTicketForm();
        if (validation == false) {
            return false
        }
        // $('#submitExhibitorForm').prop('disabled', true);
        var remark       = $('#remark').val();

        var csrfmiddlewaretoken     = $('#csrfmiddlewaretoken').val();



        var data= new FormData()

        data.append('TKT_REMARKS',remark)



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
            url: '/tickets',
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
