$( document ).ready(function() {
    var url = window.location.pathname;
    window.report_id = url.split("/")[3];
    $.ajax({
        type: 'get',
        url: '/report-map-detail-api/'+report_id,
        data: {
    
        },
        success: function (data) {
            var report=data.data
            if (report) {
                var html_array=[]
                var html=`
                <div class="row">
                    <div class="col-md-6 col-lg-6">
                        <div class="form-group row">
                            <label class="col-lg-3 col-md-3">Report ID: </label>
                            <label class="font-weight-bold col-lg-9 col-md-9 ">#`+report.REPORT.RP_ID+`</label>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-6">
                        <div class="form-group row">
                            <label class="col-lg-3 col-md-3">Report Date: </label>
                            <label class="font-weight-bold col-lg-9 col-md-9">`+report.REPORT.RP_DATE+`</label>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-6">
                        <div class="form-group row">
                            <label class="col-lg-3 col-md-3">Patient: </label>
                            <label class="font-weight-bold col-lg-9 col-md-9">`+report.REPORT.PATIENT.PT_NAME+`</label>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-6">
                        <div class="form-group row">
                            <label class="col-lg-3 col-md-3">Priority: </label>
                            <label class="font-weight-bold col-lg-9 col-md-9">`+report.REPORT.RP_PRIORITY.PRIORITY+`</label>
                        </div>
                    </div>
  
                            <div class="col-md-12 col-lg-12">
                            <div class="form-group row">
                            `
                            html_array.push(html)
                            $.each(report.REPORT_DOCUMENTS, function (i, item) { 
                                 var html1=`
                                 <div class="col-md-4 col-lg-4">
                                    <div class="form-group">
                                        <label>Report Document: </label>
                                        <a href="`+item.RP_FILE+`" download="download">
                                            <button type="button" class="btn btn-sm btn-warning">
                                                <i class="fa fa-download"></i> Download File 1
                                            </button>
                                        </a>
                                    </div>
                                    </div>
                                    <div class="col-md-3 col-lg-3" >
                                        <label>Body Part: </label>
                                        <label class="ml-5">`+item.BODY_PART.NAME+`</label>
                                    </div>
                                    <div class="col-md-3 col-lg-3" >
                                        <label>View: </label>
                                        <label class="ml-5">`+item.BODY_PART_VIEW.VIEWS_SIDE+`</label>
                                    </div>
                                 `
                                 html_array.push(html1)
                            });
                    var html2=`
                    </div>
                    </div>
                    <div class="col-md-10 col-lg-10">
                        <div class="form-group row">
                            <label class="col-lg-2 col-md-2">Remark: </label>
                            <label class="font-weight-bold col-lg-10 col-md-10">`+report.REPORT.RP_REMARKS+`</label>
                        </div>
                    </div>
                <div class="col-md-12 col-lg-12">
                <h4 class="box-title">Enter Review</h4>
            </div>
            <div class="col-md-12 col-lg-12">
                <label>Findings: </label>
                <textarea rows="5" class="form-control" placeholder="Enter Findings" id="findings">`+report.FINDINGS+`</textarea>
            </div>
            <div class="col-md-12 col-lg-12 mt-10">
                <label>Impression: </label>
                <textarea rows="5" class="form-control" placeholder="Enter Impression" id="impressions">`+report.IMPRESSIONS+`</textarea>
            </div>
            </div>
                `
                html_array.push(html2)

            }
            $('.box-body').append(html_array.join(""))
    
        },
        error: function (data) {
    
            console.log('err', data);
            obj = JSON.parse(data.responseText)
            console.log(obj.message);
            toastr.error(obj.error);
        }
    })
})
function submitReview(){
    if($('#findings').val() == "") {

        toastr.error("Please enter findings ");
        $("html").animate(
            {
              scrollTop: $('#findings').offset().top-200
            },
            800
          );
        return false;
    }
    if($('#impressions').val() == "") {

        toastr.error("Please enter impressions ");
        $("html").animate(
            {
              scrollTop: $('#impressions').offset().top-200
            },
            800
          );
        return false;
    }
    var csrf = window.CSRF_TOKEN
    var findings   = $('#findings').val();
    var impressions   = $('#impressions').val();
    var csrfmiddlewaretoken     =csrf


    var data= new FormData()

    data.append('FINDINGS',findings)
    data.append('IMPRESSIONS',impressions)
    data.append('REPORT',window.report_id)
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
        url: '/submit-review-reports-api',
        data:data,
        processData: false,
        contentType: false,

        success: function(data) {
            swal.close()
            swal("Successful", "Report review is submitted successfully ", "success").then(function() {
              window.location.href='/radiologist/reports'
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