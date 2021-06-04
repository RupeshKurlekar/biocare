$(document).ready(function () {
    $.ajax({
        type: 'get',
        url: '/add-transaction-api',
        data: {

        },
        success: function (data) {
           console.log(data.data);
           window.tran_logs=data.data
           var t= $('.transaction_log_list').DataTable( {
            "data":window.tran_logs,
            "columns": [
              { "data": null },
              { "data": "TRANS_ID"},
              { "data": "RADIOLOGIST.RDLG_ID" },
              { "data": "RADIOLOGIST.RDLG_NAME" },
              { "data": "AMOUNT" },
              { "data": "REPORTS_COUNT" },
              { "data": "REMARK" },
              { "data": null }
          ],
          columnDefs: [{
            // puts a button in the last column
            targets: [-1], render: function (a, b, data, d) {
             return  `  <a href="javascript:void(0);" >
             <button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="View" onclick="viewDetails('`+data.id+`')">
                 <i class="fa fa-eye"></i>&nbsp;View
             </button>
         </a>`
                
            },
            
        },{
            targets: [1], render: function (a, b, data, d) {
             return  `#`+data.TRANS_ID
                
            },
            
        },
        {
            targets: [2], render: function (a, b, data, d) {
             return  `#`+data.RADIOLOGIST.RDLG_ID
                
            },
            
        },
        {
          "searchable": false,
          "orderable": false,
          "targets": 0
      } 
      ],
      "order": [[ 1, 'asc' ]],
      "searching": true
      } );
      t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();
        //    if(tran_logs){
        //     $.each(tran_logs, function (i, item) { 
        //         var html=` <tr>
        //         <td>`+(i+1)+`</td>
        //         <td>#`+item.TRANS_ID+`</td>
        //         <td>#`+item.RADIOLOGIST.RDLG_ID+`</td>
        //         <td>`+item.RADIOLOGIST.RDLG_NAME+`</td>
        //         <td>`+item.AMOUNT+`</td>
        //         <td>`+item.REPORTS_COUNT+`</td>
        //         <td>
        //             `+item.REMARK+`
        //         </td>
        //         <td>
        //             <a href="javascript:void(0);" >
        //                 <button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="View" onclick="viewDetails('`+item.id+`')">
        //                     <i class="fa fa-eye"></i>&nbsp;View
        //                 </button>
        //             </a>
        //         </td>
        //     </tr>`
        //     $('.transaction_log_list').append(html)

        //     })
        //    }
          
        },
        error: function (data) {

            console.log('err', data);
            obj = JSON.parse(data.responseText)
            console.log(obj.message);
            toastr.error(obj.error);
        }
    })
})

function viewDetails(id){
    var transactions=window.tran_logs.filter(item=>{
        return item.id==id
    })
    if(transactions){
        $.each(transactions, function (i, item) { 
            $('.transaction_id').text('#'+item.TRANS_ID)
            $('.radiologist_id').text('#'+item.RADIOLOGIST.RDLG_ID)
            $('.radiologist_name').text(item.RADIOLOGIST.RDLG_NAME)
            $('.total_amt').text(item.AMOUNT)
            $('.report_count').text(item.REPORTS_COUNT)
            $('.description').text(item.REPORTS_DESCRIPTION)
            $('.remark').text(item.REMARK)
            
        });
        $('.view_modal').modal('show'); 
    }
}