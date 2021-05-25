$( document ).ready(function() {


})


    function checkRadiologistPaymentForm(form)
    {



        if($('#amount').val() == "") {

            toastr.error("Please enter amount");
            $("html").animate(
                {
                  scrollTop: $('#amount').offset().top-200
                },
                800
              );
            return false;
        }




    }



    $("#submitRadiologistPayment").click(function(){

        validation = checkRadiologistPaymentForm();
        if (validation == false) {
            return false
        }
        // $('#submitExhibitorForm').prop('disabled', true);
        var amount       = $('#amount').val();

        var csrfmiddlewaretoken     = $('#csrfmiddlewaretoken').val();



        var data= new FormData()

        data.append('RDLG_PMT_AMT',amount)



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
            url: '/rdlgpmt',
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
