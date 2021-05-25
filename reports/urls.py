from django.urls import path
from .views import ReportView, ReportDetailsView, ReportFilesView, TicketsView

urlpatterns = [
    path('reports', ReportView.as_view(), name="reports"),
    path('report/<id>', ReportDetailsView.as_view(), name="report"),
    path('rpfile', ReportFilesView.as_view(), name="rpfile"),
    path('tickets', TicketsView.as_view(), name="tickets"),

]
