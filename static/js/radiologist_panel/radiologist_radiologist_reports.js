$( document ).ready(function() {
    rdlg_id = localStorage.getItem('rdlg_id')
    getReports(rdlg_id)
    
})
function getReports(radiologist_id){
    $.ajax({
      type: 'get',
      url: '/rdlgreport-api/'+radiologist_id,
      data: {
  
      },
      success: function (data) {
          var reports=data.data
        if(reports){
          var t= $('.pending_reports').DataTable( {

            "data":reports.filter(term=>{
                return term.RP_STATUS.STATUS=="Pending"
            }),
            "columns": [
              { "data": null },
              { "data": "REPORT.RP_ID" },
              { "data": "RP_DATE" },
              { "data": "BODY_PART" },
              { "data": "BODY_PART_VIEW" },
              { "data": "REPORT.PATIENT.PT_NAME" },
              { "data": "REPORT.RP_PRIORITY.PRIORITY" },
              { "data": null }
          ],
          columnDefs: [{
            // puts a button in the last column
            targets: [-1], render: function (a, b, data, d) {
             return  `  
             <a href="javascript:void(0);"><button class="btn btn-sm btn-success mb-5" data-toggle="tooltip" data-original-title="Review" onclick="reviewReport('`+data.REPORT.id+`')"><i class="fa fa-pencil"></i>&nbsp;Review</button></a>
             <a href="javascript:void(0);"><button class="btn btn-sm btn-warning mb-5" data-toggle="tooltip" data-original-title="View" onclick="viewReport('`+data.REPORT.id+`')"><i class="fa fa-eye"></i>&nbsp;View</button></a>
         `
                
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
          var t2= $('.completed_reports').DataTable( {

            "data":reports.filter(term=>{
                return term.RP_STATUS.STATUS=="Completed"
            }),
            "columns": [
              { "data": null },
              { "data": "REPORT.RP_ID" },
              { "data": "RP_DATE" },
              { "data": "BODY_PART" },
              { "data": "BODY_PART_VIEW" },
              { "data": "REPORT.PATIENT.PT_NAME" },
              { "data": "REPORT.RP_PRIORITY.PRIORITY" },
              { "data": null }
          ],
          columnDefs: [{
            // puts a button in the last column
            targets: [-1], render: function (a, b, data, d) {
             return  `<a href="javascript:void(0);"><button class="btn btn-sm btn-warning mb-5" data-toggle="tooltip" data-original-title="View" onclick="viewReport('`+data.REPORT.id+`')"><i class="fa fa-eye"></i>&nbsp;View</button></a>`
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
      t2.on( 'order.dt search.dt', function () {
        t2.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();
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
  function reviewReport(id){
      window.location.href='/radiologist/review_report/'+id
  }
  function viewReport(id){
      window.location.href='/radiologist/view_report/'+id
  }