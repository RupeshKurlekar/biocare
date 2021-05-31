$( document ).ready(function() {
    tech_id = localStorage.getItem('tech_id')
    getPriority()

})

      function getPriority(){
        $.ajax({
          type: 'get',
          url: '/priority',
          data: {
      
          },
          success: function (data) {
              var priority_master_list=data.data
              console.log('',);
              if (priority_master_list) {
                  $.each(priority_master_list, function (i, item) { 
                      if (item.){
                   var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                   <td>#`+item.PRIORITY+`</td>
                   <td>`+item.DURATION+`</td>
                   <td>`+item.RATE+`</td>

                  <td>
                  <a href="javascript:void(0);" data-toggle="modal" data-target=".editModal"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Edit</button></a>
    
                  <button class="btn btn-sm btn-danger delRow" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash"></i>&nbsp;Delete</button>
                    </td>
               </tr>`

                 }
                  
                  
               });
       
               }
               
       
           },
           error: function (data) {
       
               console.log('err', data);
               obj = JSON.parse(data.responseText)
               console.log(obj.message);
               toastr.error(obj.error);
           }
       })
       }