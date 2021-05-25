from django.urls import path
from .views import RadiologistView, RadiologistReportMapView, RadiologistReportFilesView, RadiologistPmtView

urlpatterns = [
    path('radiologists', RadiologistView.as_view(), name="radiologists"),
    path('rdlgreport', RadiologistReportMapView.as_view(), name="rdlgreport"),
    path('rdlgfile', RadiologistReportFilesView.as_view(), name="rdlgfile"),
    path('rdlgpmt', RadiologistPmtView.as_view(), name="rdlgpmt"),

]
