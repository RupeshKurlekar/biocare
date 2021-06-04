from django.urls import path
from .views import PatientView, PatientHistoryView, PatientHistoryFilesView, PatientHistoryDetailsView, \
    PatientDetailsView,PatientsPage,PatientUpdateView,DeletePatientView,RadiologistPatientHistoryPage

urlpatterns = [
    path('patients-api', PatientView.as_view(), name="patients-api"),
    path('delete-patient-api/<id>', DeletePatientView.as_view(), name="delete-patient-api"),
    path('patients-update-api', PatientUpdateView.as_view(), name="patients-update-api"),
    path('patient/<id>', PatientDetailsView.as_view(), name="patient"),
    path('pthistory', PatientHistoryView.as_view(), name="pthistory"),
    path('pthsfile', PatientHistoryFilesView.as_view(), name="pthsfile"),
    path('pthsfiledetails/<id>', PatientHistoryDetailsView.as_view(), name="pthsfiledetails"),
    path('<type>/patients',PatientsPage.as_view(),name='patients'),
    path('radiologist/send_patient_history',RadiologistPatientHistoryPage.as_view(),name='radiologist_send_patient_history'),

]
