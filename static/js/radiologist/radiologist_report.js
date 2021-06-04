$( document ).ready(function() {
    var url = window.location.pathname;
    var radiologist_id = url.split("/")[2];
    getReports(radiologist_id)
})

function getReports(radiologist_id){
    $.ajax({
      type: 'get',
      url: '/rdlgreport-api/'+radiologist_id,
      data: {
  
      },
      success: function (data) {
          var reports=data.data
          console.log('reports',reports);
          var t= $('.radiologist_reports').DataTable( {
            "data":reports,
            "columns": [
              { "data": null },
              { "data": "REPORT.RP_ID" },
              { "data": "RP_DATE" },
              { "data": "BODY_PART" },
              { "data": "BODY_PART_VIEW" },
              { "data": "REPORT.PATIENT.PT_NAME" },
              { "data": "REPORT.RP_PRIORITY.PRIORITY" },
              { "data": "RP_STATUS.STATUS" },
              { "data": null }
          ],
          columnDefs: [{
            // puts a button in the last column
            targets: [-1], render: function (a, b, data, d) {
             return  `  <a href="javascript:void(0);" onclick="openReportDetails('`+data.REPORT.id+`')"><button class="btn btn-sm btn-warning mb-5" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View</button></a>`
                
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
        //   if (reports) {
        //       $.each(reports, function (i, item) { 
        //        var html=`<tr>
            
        //        <td>`+(i+1)+`</td>
        //        <td>#`+item.REPORT.RP_ID+`</td>
        //        <td>`+item.RP_DATE+`</td>
        //        <td>`+item.BODY_PART+`</td>
        //        <td>`+item.BODY_PART_VIEW+`</td>
        //        <td>`+item.REPORT.PATIENT.PT_NAME+`</td>
        //        <td>`+item.REPORT.RP_PRIORITY.PRIORITY+`</td>
        //        <td>`+item.RP_STATUS.STATUS+`</td>
        //       <td>
        //            <a href="javascript:void(0);" onclick="openReportDetails('`+item.REPORT.id+`')"><button class="btn btn-sm btn-warning mb-5" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View</button></a>
        //        </td>
        //    </tr>` 
        //      $('.radiologist_reports').append(html)

        //   });
  
        //   }
          
  
      },
      error: function (data) {
  
          console.log('err', data);
          obj = JSON.parse(data.responseText)
          console.log(obj.message);
          toastr.error(obj.error);
      }
  })
  }

  function openReportDetails(report_id){
    window.location.href='/view_radiologist_report/'+report_id

}