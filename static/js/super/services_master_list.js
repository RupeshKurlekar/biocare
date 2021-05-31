$( document ).ready(function(){
    getServices()
})

      function getServices(){
        $.ajax({
            type: 'get',
            url: '/body_parts',
            data: {
        
            },
            success: function (data){
                var services_master_list=data.data
                $.each(services_master_list, function (i, item){
                    var html=`<tr>
                   <td>
                   </td>
                   <td>`+(i+1)+`</td>
                   <td>#`+item.NAME+`</td>
                  <td>
                  <a href="javascript:void(0);" data-toggle="modal" data-target=".editModal"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Edit</button></a>
    
                  <button class="btn btn-sm btn-danger delRow" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash"></i>&nbsp;Delete</button></td>
                </tr>`
                    $('.super_services_master').append(html)
                
                })

            },
            error: function (data) {
       
                console.log('err', data);
                obj = JSON.parse(data.responseText)
                console.log(obj.message);
                toastr.error(obj.error);
            }
                })

                $.ajax({
                    type: 'get',
                    url: '/body_parts_views',
                    data: {
                
                    },
                    success: function (data){
                        var services_master_list=data.data
                        $.each(services_master_list, function (i, item){
                            var html=`<tr>
                           <td>
                           </td>
                           <td>`+(i+1)+`</td>
                           <td>#`+item.VIEWS_SIDE+`</td>
                          <td>
                          <a href="javascript:void(0);" data-toggle="modal" data-target=".editModal"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="Edit"><i class="fa fa-pencil"></i>&nbsp;Edit</button></a>
            
                          <button class="btn btn-sm btn-danger delRow" data-toggle="tooltip" data-original-title="Delete"><i class="fa fa-trash"></i>&nbsp;Delete</button></td>
                        </tr>`
                            $('.bodypart_view').append(html)
                        
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


      
        


