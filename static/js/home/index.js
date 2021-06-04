$( document ).ready(function() {
    var instance = $('.skeleton').scheletrone();
    var url = window.location.pathname;
    var type = url.split("/")[1];
    getStats(type)
})

function getStats(type){
    $.ajax({
      type: 'get',
      url: '/homepage-stats-api/'+type,
      data: {
  
      },
      success: function (data) {
          var stats=data.data
          var html_array=[]
          $.each(stats, function (i, item)  { 
         console.log(i)

            $.each(item, function (key, val) {
          if(key=='High'){
            console.log(val);
        var html=`	<div class="col-xl-4 col-md-6 col-12">

        <div class="box box-widget widget-user-2">
            <div class="widget-user-header bg-danger">
                <h3 class="widget-user-username ml-0">
                    <i class="font-size-30 fa fa-file-text-o"></i>
                    <span class="head_dash_span">Urgent Priority Reports </span>
                    <h6 class="widget-user-desc urgent_priority_reports">`+val.total_reports+`</h6>
                </h3>
            </div>
            <div class="box-footer no-padding">
                <ul class="nav d-block nav-stacked">
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Total reports assigned to doctor

                            </span>
                            <span class="pull-right badge bg-info">
                                <h4 class="mb-0 urgent_total_reports">`+val.assigned_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Report Pending
                            </span>
                            <span class="pull-right badge bg-success">
                                <h4 class="mb-0 urgent_pending_reports">`+val.pending_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Today's Reports
                            </span>
                            <span class="pull-right badge bg-warning">
                                <h4 class="mb-0 urgent_todays_reports">`+val.todays_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Completed Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0 urgent_completed_reports">`+val.completed_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Current Week Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0 urgent_current_week_reports">`+val.weekly_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Newly Generated Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0 urgent_new_reports">`+val.pending_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Requested Ticket Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0 urgent_tickets_reports">`+val.requested_ticket_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Requested for patient history
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0 ">0</h4>
                            </span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>  

    </div>   `
    html_array.push(html)

    }
    else if(key=='Medium'){
       var html2= `<div class="col-xl-4 col-md-6 col-12">

        <div class="box box-widget widget-user-2">
            <div class="widget-user-header bg-warning">
                <h3 class="widget-user-username ml-0">
                    <i class="font-size-30 fa fa-file-text-o"></i>
                    <span class="head_dash_span">Medium Priority Reports </span>
                    <h6 class="widget-user-desc urgent_total_reports">`+val.total_reports+`</h6>
                </h3>
            </div>
            <div class="box-footer no-padding">
                <ul class="nav d-block nav-stacked">
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Total reports assigned to doctor
                            </span>
                            <span class="pull-right badge bg-info">
                                <h4 class="mb-0 urgent_pending_reports">`+val.assigned_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Report Pending
                            </span>
                            <span class="pull-right badge bg-success">
                                <h4 class="mb-0">`+val.pending_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Today's Reports
                            </span>
                            <span class="pull-right badge bg-warning">
                                <h4 class="mb-0">`+val.todays_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Completed Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.completed_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Current Week Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.weekly_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Newly Generated Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.pending_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Requested Ticket Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.requested_ticket_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Requested for patient history
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">0</h4>
                            </span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>  
                                
    </div>`
    html_array.push(html2)


    }
    else if(key=='Low'){
        var html3=`
        <div class="col-xl-4 col-md-6 col-12">

        <div class="box box-widget widget-user-2">
            <div class="widget-user-header bg-info">
                <h3 class="widget-user-username ml-0">
                    <i class="font-size-30 fa fa-file-text-o"></i>
                    <span class="head_dash_span">Low Priority Reports </span>
                    <h6 class="widget-user-desc">`+val.total_reports+`</h6>
                </h3>
            </div>
            <div class="box-footer no-padding">
                <ul class="nav d-block nav-stacked">
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Total reports assigned to doctor
                            </span>
                            <span class="pull-right badge bg-info">
                                <h4 class="mb-0">`+val.assigned_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Report Pending
                            </span>
                            <span class="pull-right badge bg-success">
                                <h4 class="mb-0">`+val.pending_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Today's Reports
                            </span>
                            <span class="pull-right badge bg-warning">
                                <h4 class="mb-0">`+val.todays_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Completed Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.completed_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Current Week Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.weekly_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Newly Generated Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.pending_reports+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Requested Ticket Reports
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">`+val.requested_ticket_report+`</h4>
                            </span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/#" class="nav-link">
                            <span class="font_dashboard_span">
                                Requested for patient history
                            </span>
                            <span class="pull-right badge bg-danger">
                                <h4 class="mb-0">0</h4>
                            </span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>  
                                
    </div>  
        `
        html_array.push(html3)

    }
});

})
var instance = $('.skeleton').scheletrone('stopLoader');
$('.stats_row').append(html_array.join(""))
      },
      error: function (data) {
  
          console.log('err', data);
          obj = JSON.parse(data.responseText)
          console.log(obj.message);
          toastr.error(obj.error);
      }
  })
  }