$(document).ready(function () {
    tech_id = localStorage.getItem('tech_id')
    $.ajax({
        type: 'get',
        url: '/wallet-api/'+tech_id,
        data: {

        },
        success: function (data) {
            window.IsAmountPresent=data.IsAmountPresent;
            window.WALLET_AMT=data.data.WALLET_AMT
            if(data.IsAmountPresent){
                $('.wallet_amount').append(`Wallet Amount : `+data.data.WALLET_AMT)
            }
            else{
                $('.wallet_amount').append(`Wallet Amount : 0`)
            }
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
        url: '/pay-radiologist-list-api/'+tech_id,
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
                  { "data": "total_amount" },
                  { "data": "total_due_amount" },
                  { "data": "total_reports" },
                  { "data": null }
              ],
              columnDefs: [{
                // puts a button in the last column
                targets: [-1], render: function (a, b, data, d) {
                 return  ` <a href="javascript:void(0);" >
                 <button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="Pay" onclick="openRadiologistPaymentModal(`+data.RADIOLOGIST.id+`,'`+data.RADIOLOGIST.RDLG_ID+`','`+data.RADIOLOGIST.RDLG_NAME+`','`+data.total_due_amount+`','`+data.total_reports+`')">
                     <i class="fa fa-send"></i>&nbsp;Pay
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
          "order": [[ 1, 'asc' ]],
          "searching": true
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
            //         <td>#`+item.RADIOLOGIST.RDLG_ID+`</td>
            //         <td>`+item.RADIOLOGIST.RDLG_NAME+`</td>
            //         <th>`+item.total_amount+`</th>
            //         <th>`+item.total_due_amount+`</th>
            //         <th>`+item.total_reports+`</th>
            //         <td>
            //         <a href="javascript:void(0);" >
            //             <button class="btn btn-sm btn-warning" data-toggle="tooltip" data-original-title="Pay" onclick="openRadiologistPaymentModal(`+item.RADIOLOGIST.id+`,'`+item.RADIOLOGIST.RDLG_ID+`','`+item.RADIOLOGIST.RDLG_NAME+`','`+item.total_due_amount+`','`+item.total_reports+`')">
            //                 <i class="fa fa-send"></i>&nbsp;Pay
            //             </button>
            //         </a>
            //     </td>
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

function openRadiologistPaymentModal(id,RDLG_ID,RDLG_NAME,DUE_AMT,TOTAL_REPORTS){
    $('.pay_modal').modal('show')
    $('.radiologist_id').text(`#`+RDLG_ID)
    $('.radiologist_name').text(RDLG_NAME)
    window.RADIOLOGIST_ID=id
    window.DUE_AMT=DUE_AMT
    window.TOTAL_REPORTS=TOTAL_REPORTS


}
function payRadiologist(){
    if($('#total_amount').val()==""){
        toastr.error("Please enter total amount")
        return false
    }
    else{
        if(parseInt($('#total_amount').val())>window.DUE_AMT){
            toastr.error("Please enter  amount less than due amount")
            return false

        }
        else if (parseInt($('#total_amount').val())>window.WALLET_AMT){
            toastr.error("Not enough amount in wallet")
            return false
        }
    }
    
    if($('#total_count').val()==""){
        toastr.error("Please enter reports count")
        return false
    }
    else{
        if(parseInt($('#total_count').val())>window.TOTAL_REPORTS){
            toastr.error("Please enter valid reports count")
            return false

        }
    }
    if($('#report_description').val()==""){
        toastr.error("Please enter report description")
        return false
    }
    var csrf = window.CSRF_TOKEN

    var total_amount   = $('#total_amount').val();
    var total_count     = $('#total_count').val();
    var report_description     = $('#report_description').val();
    var report_remark   = $('#report_remark').val();
    var csrfmiddlewaretoken     =csrf
    var tech_id = localStorage.getItem('tech_id')


    var data= new FormData()

    data.append('RADIOLOGIST',window.RADIOLOGIST_ID)
    data.append('AMOUNT',total_amount)
    data.append('REPORTS_COUNT',total_count)
    data.append('REPORTS_DESCRIPTION',report_description)
    data.append('REMARK',report_remark)
    data.append('TECHNICIAN',tech_id)

    data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
    console.log('daaaa',data)
    swal({
        title: 'Please Wait',
        allowEscapeKey: false,
        allowOutsideClick: false,
        showLoaderOnConfirm: true,
        buttons: false

      })
    $.ajax({
        type: 'post',
        url: '/add-transaction-api',
        data:data,
        processData: false,
        contentType: false,

        success: function(data) {
            swal.close()
             swal("Successful", "Payment successfull  ", "success").then(function() {
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
               console.log(obj);
               console.log(obj.message);
               if (obj.error){
                toastr.error(obj.error);
               }
               else{
                toastr.error(obj.message);

               }
          }
          }
      });
}