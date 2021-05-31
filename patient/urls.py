from django.urls import path
from .views import PatientView, PatientHistoryView, PatientHistoryFilesView, PatientHistoryDetailsView, \
    PatientDetailsView,PatientsPage,PatientUpdateView

urlpatterns = [
    path('patients-api', PatientView.as_view(), name="patients-api"),
    path('patients-update-api', PatientUpdateView.as_view(), name="patients-update-api"),
    path('patient/<id>', PatientDetailsView.as_view(), name="patient"),
    path('pthistory', PatientHistoryView.as_view(), name="pthistory"),
    path('pthsfile', PatientHistoryFilesView.as_view(), name="pthsfile"),
    path('pthsfiledetails/<id>', PatientHistoryDetailsView.as_view(), name="pthsfiledetails"),
    path('<type>/patients/',PatientsPage.as_view(),name='patients')

]
