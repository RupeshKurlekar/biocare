from django.urls import path
from .views import ReportView, ReportDetailsView, ReportFilesView, TicketsView, ReportsPage, AddReportsPage, ReportDetailsPage, EditReportsPage, EditReportsView, TicketsPage, DeleteReportView,AssignReportsAPIView,AssignMultipleReportsAPIView,SubmitReportReviewAPI

urlpatterns = [
    path('reports-api', ReportView.as_view(), name="reports-api"),
    path('<type>/reports', ReportsPage.as_view(), name="reports"),
    path('add_report', AddReportsPage.as_view(), name="add_report"),
    path('edit_report/<id>', EditReportsPage.as_view(), name="edit_report"),
    path('edit-reports-api/<id>', EditReportsView.as_view(), name="edit_report_api"),
    path('report-api/<id>', ReportDetailsView.as_view(), name="report"),
    path('delete-report-api/<id>', DeleteReportView.as_view(), name="delete_report"),
    path('report/<id>', ReportDetailsPage.as_view(), name="report_details"),
    path('rpfile', ReportFilesView.as_view(), name="rpfile"),
    path('tickets-api', TicketsView.as_view(), name="tickets"),
    path('assign-reports-api', AssignReportsAPIView.as_view(), name="assign-reports-api"),
    path('assign-multiple-reports-api', AssignMultipleReportsAPIView.as_view(), name="assign-multiple-reports-api"),
    path('submit-review-reports-api', SubmitReportReviewAPI.as_view(), name="submit-review-reports-api"),
    path('technician/tickets', TicketsPage.as_view(), name="technician_tickets"),

]
