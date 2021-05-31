$( document ).ready(function() {
    tech_id = localStorage.getItem('tech_id')
    getTechnician()

})

      function getTechnician(){
        $.ajax({
          type: 'get',
          url: '/technicians',
          data: {
      
          },
          success: function (data) {
              var technician_view=data.data
              console.log('',);
              if (technician_view) {
                  $.each(technician_view, function (i, item) { 
                      if (item.IS_APPROVED==false){
                   var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                   <td>#`+item.TECH_ID+`</td>
                   <td>`+item.TECH_NAME+`</td>
                   <td>`+item.TECH_MOB+`</td>
                   <td>`+item.TECH_EMAIL+`</td>
                   <td>`+item.TECH_ADDRESS+`</td>

                  <td>
                    <a href="javascript:void(0);" data-toggle="modal" data-target=".editModal"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Edit</button></a>
                    <a href="javascript:void(0);" data-toggle="modal" data-target=".viewModal"><button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View</button></a>
                    <a href="technician-patientslist.php"><button class="btn btn-sm btn-info" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View Patients</button></a>
                    <button class="btn btn-sm btn-danger delRow" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash"></i>&nbsp;Delete</button>
                    </td>
               </tr>`
               $('.super_technician').append(html)

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