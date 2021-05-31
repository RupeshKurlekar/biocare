$( document ).ready(function() {
    getPatients()

})

      function getPatients(){
        $.ajax({
            type: 'get',
            url: '/patients',
            data: {
        
            },
            success: function (data){
                var patients_list=data.data
                $.each(patients_list, function (i, item){
                    var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                   <td>#`+item.PT_ID+`</td>
                   <td>#`+item.PT_NAME+`</td>
                   <td>#`+item.PT_AGE+`</td>
                   <td>#`+item.PT_GENDER+`</td>
                  <td>
                  <a href="javascript:void(0);" data-toggle="modal" data-target=".editModal"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Edit</button></a>
                    <a href="javascript:void(0);" data-toggle="modal" data-target=".viewModal"><button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View</button></a>
                    <button class="btn btn-sm btn-danger delRow" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash"></i>&nbsp;Delete</button></td>
                </tr>`
                    $('.patients').append(html)
                
                })

            },
            error: function (data) {
       
                console.log('err', data);
                obj = JSON.parse(data.responseText)
                console.log(obj.message);
                toastr.error(obj.error);
            }
                })
    
}