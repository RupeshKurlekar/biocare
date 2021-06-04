$( document ).ready(function() {
    window.rdlg_id = localStorage.getItem('rdlg_id')
})

function submitPassword(){
    if($('#old_password').val()==""){
        toastr.error("Please enter old password")
        return false
    }
    if($('#new_password1').val()==""){
        toastr.error("Please enter new password")
        return false
    }
    if($('#new_password2').val()==""){
        toastr.error("Please enter new  password")
        return false
    }
    if($('#new_password1').val() !=$('#new_password2').val()){
        toastr.error("Password do not match")
        return false
    }
    var csrf = window.CSRF_TOKEN
    var old_password   = $('#old_password').val();
    var new_password   = $('#new_password1').val();
    console.log(new_password);
   
    var csrfmiddlewaretoken     =csrf
    var data= new FormData()
    data.append('RDLG_OLD_PASSWORD',old_password)
    data.append('RDLG_PASSWORD',new_password)
    data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
    swal({
        title: 'Please Wait',
        allowEscapeKey: false,
        allowOutsideClick: false,
        showLoaderOnConfirm: true,
        buttons: false

      })
    $.ajax({
        type: 'post',
        url: '/radiologist-change-password-api/'+window.rdlg_id,
        data:data,
        processData: false,
        contentType: false,

        success: function(data) {
            swal.close()
             swal("Successful", "Password changed successfully  ", "success").then(function() {
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