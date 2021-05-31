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
              var radiologist_appr=data.data
              console.log('',);
              if (radiologist_appr) {
                  $.each(radiologist_appr, function (i, item) { 
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
                  <td>
                  <a href="javascript:void(0);" data-toggle="modal" data-target="#modified"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;modified</button></a>

                  <a href="javascript:void(0);" data-toggle="modal" data-target=".viewModal"><button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-eye"></i>&nbsp;view</button></a></td>
              </tr>`
                 $('.new_radiologist_approval').append(html)
                      }
                else if(item.IS_APPROVED){
                    var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                  <td>#`+item.RDLG_ID+`</td>
                   <td>`+item.RDLG_NAME+`</td>
                   <td>`+item.RDLG_MOB_NO+`</td>
                   <td>`+item.RDLG_EMAIL+`</td>
                   <td>`+item.RDLG_SPECIALITY+`</td>
                  <td>
                  <a href="#"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Approved</button></a></td> -->
               </tr>`
                 $('.radiologist_approved').append(html)

                }
    
                 else{var html=`<tr>
                 <td>
                 </td>
                 <td>`+(i+1)+`</td>
                 <td>#`+item.RDLG_ID+`</td>
                 <td>`+item.RDLG_NAME+`</td>
                 <td>`+item.RDLG_MOB_NO+`</td>
                 <td>`+item.RDLG_EMAIL+`</td>
                 <td>`+item.RDLG_SPECIALITY+`</td>
               </tr> ` 
               $('.all_radiologist_approval').append(html)

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
