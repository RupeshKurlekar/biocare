from django.urls import path
from .views import ReportStatusView, PriorityView, TicketStatusView, BodyParts, BodyPartViewsView 
urlpatterns = [
    path('report_status', ReportStatusView.as_view(), name="report_status"),
    path('priority', PriorityView.as_view(), name="priority"),
    path('ticket_status', ReportStatusView.as_view(), name="ticket_status"),
    path('body_parts', BodyParts.as_view(), name="body_parts"),
    path('body_parts_views', BodyPartViewsView.as_view(), name="body_parts_views"),
]