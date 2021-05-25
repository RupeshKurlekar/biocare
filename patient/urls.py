from django.urls import path
from .views import PatientView, PatientHistoryView, PatientHistoryFilesView, PatientHistoryDetailsView, \
    PatientDetailsView

urlpatterns = [
    path('patients', PatientView.as_view(), name="patients"),
    path('patient/<id>', PatientDetailsView.as_view(), name="patient"),
    path('pthistory', PatientHistoryView.as_view(), name="pthistory"),
    path('pthsfile', PatientHistoryFilesView.as_view(), name="pthsfile"),
    path('pthsfiledetails/<id>', PatientHistoryDetailsView.as_view(), name="pthsfiledetails"),

]
