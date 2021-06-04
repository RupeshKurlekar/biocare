$( document ).ready(function() {
    super_id = localStorage.getItem('super_id')
    $.ajax({
        type: 'get',
        url: '/super-detail-view-api/'+super_id,
        data: {

        },
        success: function (data) {
            console.log(data.data)
            var superprofile = data.data;
            if (superprofile) {
                $('.super_name').html(super.SUPER_NAME)
                $('.email_address').html(super.SUPER_EMAIL);
                $('.mobile_number').html(super.SUPER_MOB);
                $('.address_val').html(super.SUPER_ADDRESS);
                $('.profile_image').attr('src',super.TECH_IMG);
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