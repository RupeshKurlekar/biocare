$( document ).ready(function() {
    getAllreports()

})

      function getAllreports(){
        $.ajax({
            type: 'get',
            url: '/reports',
            data: {
        
            },
            success: function (data){}}}