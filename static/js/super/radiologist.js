$( document ).ready(function() {
    tech_id = localStorage.getItem('tech_id')
    getRadiologist()

})

      function getRadiologist(){
        $.ajax({
          type: 'get',
          url: '/radiologists-api',
          data: {
      
          },
          success: function (data) {
              var radiologist_view=data.data
              console.log('',);
              if (radiologist_view) {
                  $.each(radiologist_view, function (i, item) { 
                      if (item.IS_APPROVED==false){
                   var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                   <td>#`+item.RDLG_ID+`</td>
                   <td>`+item.RDLG_NAME+`</td>
                   <td>`+item.RDLG_MOB_NO+`</td>
                   <td>`+item.RDLG_EMAIL+`</td>
                   <td>`+item.RDLG_SPECIALITY+`</td>
                   <td>`+item.RDLG_ADDRESS+`</td>
                  <td>
                    <a href="javascript:void(0);" data-toggle="modal" data-target=".editModal"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Edit</button></a>
                    <a href="javascript:void(0);" data-toggle="modal" data-target=".viewModal"><button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View</button></a>
                    <button class="btn btn-sm btn-danger delRow" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash"></i>&nbsp;Delete</button>
              </tr>`
                 $('.super_radiologist').append(html)
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
