$(document).ready(function () {
    tech_id = localStorage.getItem('tech_id')
    $.ajax({
        type: 'get',
        url: '/rdlgreporttechnician/'+tech_id,
        data: {

        },
        success: function (data) {
            console.log(data.data)
            window.radiologists = data.data;
            var t= $('.radiologist_list').DataTable( {
                "data":window.radiologists,
                "columns": [
                  { "data": null },
                  { "data": "RADIOLOGIST.RDLG_ID" },
                  { "data": "RADIOLOGIST.RDLG_NAME" },
                  { "data": null }
              ],
              columnDefs: [{
                // puts a button in the last column
                targets: [-1], render: function (a, b, data, d) {
                 return  ` <a href="javascript:void(0);">
                 <button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="View Reports" onclick="openRadiologistReport(`+data.RADIOLOGIST.id+`)">
                     <i class="fa fa-eye"></i>&nbsp;View Reports
                 </button>
             </a>`
                    
                },
                
            },
            {
              "searchable": false,
              "orderable": false,
              "targets": 0
          } 
          ],
          "order": [[ 1, 'asc' ]]
          } );
          t.on( 'order.dt search.dt', function () {
            t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
                cell.innerHTML = i+1;
            } );
        } ).draw();
            // if (radiologists) {
            //     console.log('2');
            //     $.each(radiologists, function (i, item) { 
            //         var html = `<tr>
            //         <td>`+(i+1)+`</td>
            //         <td>`+item.RADIOLOGIST.RDLG_ID+`</td>
            //         <td>`+item.RADIOLOGIST.RDLG_NAME+`</td>
            //         <td>
            //             <a href="javascript:void(0);">
            //                 <button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="View Reports" onclick="openRadiologistReport(`+item.RADIOLOGIST.id+`)">
            //                     <i class="fa fa-eye"></i>&nbsp;View Reports
            //                 </button>
            //             </a>
            //         </td>
            //     </tr>`
            //    $('.radiologist_list').append(html)

            // });

            // }
            // else{
            //     // console.log('1');
            //     // $('.radiologist_list').append('No patients added')

            // }

        },
        error: function (data) {

            console.log('err', data);
            obj = JSON.parse(data.responseText)
            console.log(obj.message);
            toastr.error(obj.error);
        }
    })
})
function openRadiologistReport(radiologist_id){
    window.location.href='/rdlgreport/'+radiologist_id

}