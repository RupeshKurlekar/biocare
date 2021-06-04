$( document ).ready(function() {
    rdlg_id = localStorage.getItem('rdlg_id')
    getPatients(rdlg_id)
    getPatientsHistory(rdlg_id)
    
})
function getPatients(radiologist_id){
    $.ajax({
        type: 'get',
        url: '/radiologist_patients/'+radiologist_id,
        data: {

        },
        success: function (data) {

            console.log(data.data)
            window.patients = data.data;
            if (patients) {
                $.each(patients, function (i, item) { 
                       
                 var html=`<option value="`+item.id+`">`+item.PT_NAME+` (`+ item.PT_MOB+`)</option>` 
               
                 $('#patients').append(html)
  
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
  function submitRequestHistory(){
    if($('#patients').val() == "") {

        toastr.error("Please select patient");
        $("html").animate(
            {
              scrollTop: $('#patients').offset().top-200
            },
            800
          );
        return false;
    }
   
    var csrf = window.CSRF_TOKEN
    var patients   = $('#patients').val();
    var ptnt_hist_title   = $('#ptnt_hist_title').val();
    var csrfmiddlewaretoken     =csrf


    var data= new FormData()

    data.append('PATIENT',patients)
    data.append('RP_REMARKS',ptnt_hist_title)
    data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
    swal({
        title: 'Please Wait',
        allowEscapeKey: false,
        allowOutsideClick: false,
        showLoaderOnConfirm: true,
        buttons: false

      })
    $.ajax({
        type: 'post',
        url: '/pthistory',
        data:data,
        processData: false,
        contentType: false,

        success: function(data) {
            swal.close()
            swal("Successful", "Patient history request is submitted successfully ", "success").then(function() {
              location.reload()
            });
            },
          error: function(data) {
            console.log(data)
            swal.close()
            if (data.status == 403) {
            toastr.options = {
                positionClass: 'toast-top-center'
            };
            toastr.error("Please refresh your page!!!");
        }
        else{

               obj = JSON.parse(data.responseText)
               $.each(obj.message, function (i, item) { 
                $.each(item, function (j, iter) { 
                toastr.error(iter);

                })
               });
           
          }
          }
      });
}
function getPatientsHistory(radiologist_id){
    $.ajax({
      type: 'get',
      url: '/radiologist_patients_history/'+radiologist_id,
      data: {
  
      },
      success: function (data) {
          var history=data.data
          window.history_data=data.data

        if(history){
          var t= $('.pending_history').DataTable( {

            "data":history.filter(term=>{
                return term.IS_SENT==false
            }),
            "columns": [
                { "data": null },
                { "data": "PT_HSTY_ID" },
                { "data": "PATIENT.PT_ID" },
                { "data": "PATIENT.PT_NAME" },
                { "data": null }
          ],
          columnDefs: [{
            // puts a button in the last column
            targets: [-1], render: function (a, b, data, d) {
                return  `<a href="javascript:void(0);" data-toggle="modal"  onclick="viewHistory(`+data.id+`)"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View</button></a>
                `
               }
            
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
          var t2= $('.completed_history').DataTable( {

            "data":history.filter(term=>{
                return term.IS_SENT
            }),
            "columns": [
                { "data": null },
                { "data": "PT_HSTY_ID" },
                { "data": "PATIENT.PT_ID" },
                { "data": "PATIENT.PT_NAME" },
                { "data": null }
          ],
          columnDefs: [{
            // puts a button in the last column
            targets: [-1], render: function (a, b, data, d) {
             return  `<a href="javascript:void(0);" data-toggle="modal"  onclick="viewHistory(`+data.id+`)"><button class="btn btn-sm btn-success" data-toggle="tooltip" data-original-title="View"><i class="fa fa-eye"></i>&nbsp;View</button></a>
             `
            }
            
            
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
  function viewHistory(id){
      var patient=window.history_data.filter(item=>{
          return item.id==id
      })
    $.each(patient, function (i, item) { 
        $('.patient_title_modal').text(item.RP_REMARKS)
        $('.patient_name_modal').text(item.PATIENT.PT_NAME)
  
        
    });
    $('.viewHistory').modal('show'); 
  }