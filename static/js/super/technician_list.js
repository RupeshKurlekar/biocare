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
              var technician_appr=data.data
              console.log('',);
              if (technician_appr) {
                  $.each(technician_appr, function (i, item) { 
                      if (item.IS_APPROVED==false){
                   var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                   <td>#`+item.TECH_ID+`</td>
                   <td>`+item.TECH_NAME+`</td>
                   <td>`+item.TECH_MOB+`</td>
                   <td>`+item.TECH_EMAIL+`</td>
                  <td>
                       <a href="javascript:void(0);" data-toggle="modal" data-target="#modified"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;modified</button></a>

                       <a href="javascript:void(0);" data-toggle="modal" data-target=".viewModal"><button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-eye"></i>&nbsp;view</button></a></td>
    
    
                       <button class="btn btn-sm btn-danger delRow mb-5" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash"></i>&nbsp;Delete</button>
                   </td>
               </tr>`
                 $('.new_technician_apr').append(html)
                      }
                else if(item.IS_APPROVED){
                    var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                   <td>#`+item.TECH_ID+`</td>
                   <td>`+item.TECH_NAME+`</td>
                   <td>`+item.TECH_MOB+`</td>
                   <td>`+item.TECH_EMAIL+`</td>
                  <td>
                    <a href="#"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Approved</button></a></td> -->
    
                   </td>
               </tr>`
                 $('.approved_technician_apr').append(html)

                }
    
                 else{var html=`<tr>
                 <td>
                 </td>
                 <td>`+(i+1)+`</td>
                 <td>#`+item.TECH_ID+`</td>
                 <td>`+item.TECH_NAME+`</td>
                 <td>`+item.TECH_MOB+`</td>
                 <td>`+item.TECH_EMAIL+`</td>
                
             </tr>` 
               $('.all_technician_apr').append(html)

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