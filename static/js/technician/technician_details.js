$( document ).ready(function() {
    tech_id = localStorage.getItem('tech_id')
    $.ajax({
        type: 'get',
        url: '/technician_details/'+tech_id,
        data: {

        },
        success: function (data) {
            console.log(data.data)
            var technician = data.data;
            if (technician) {
                $('.tech_name').html(technician.TECH_NAME)
                $('.email_address').html(technician.TECH_EMAIL);
                $('.mobile_number').html(technician.TECH_MOB);
                $('.address_val').html(technician.TECH_ADDRESS);
                $('.profile_image').attr('src',technician.TECH_IMG);
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