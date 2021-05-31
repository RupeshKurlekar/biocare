from django.urls import path
from .views import ReportView, ReportDetailsView, ReportFilesView, TicketsView, ReportsPage, AddReportsPage, ReportDetailsPage, EditReportsPage,EditReportsView

urlpatterns = [
    path('reports-api', ReportView.as_view(), name="reports-api"),
    path('<type>/reports', ReportsPage.as_view(), name="reports"),
    path('add_report', AddReportsPage.as_view(), name="add_report"),
    path('edit_report/<id>', EditReportsPage.as_view(), name="edit_report"),
    path('edit_report-api/<id>', EditReportsView.as_view(), name="edit_report_api"),
    path('report-api/<id>', ReportDetailsView.as_view(), name="report"),
    path('report/<id>', ReportDetailsPage.as_view(), name="report_details"),
    path('rpfile', ReportFilesView.as_view(), name="rpfile"),
    path('tickets', TicketsView.as_view(), name="tickets"),

]
