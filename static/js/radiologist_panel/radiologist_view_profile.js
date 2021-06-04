
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
                $('#full_name').text(radiologist.RDLG_NAME)
                $('#email').text(radiologist.RDLG_EMAIL);
                $('#mobile_no').text(radiologist.RDLG_MOB_NO);
                $('#address').text(radiologist.RDLG_ADDRESS);
                $('#profile_image').attr('src',radiologist.RDLG_IMG);
                $('#qualification').text(radiologist.RDLG_QUALIFICATION);
                $('#experience').text(radiologist.RDLG_EXPERIENCE);
                $('#speciality').text(radiologist.RDLG_SPECIALITY);
                $('#radiologist_area').text(radiologist.RDLG_AREA);
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
