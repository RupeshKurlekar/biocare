from django.contrib import admin
from .models import Patient, PatientHistory, PatientHistoryFiles

# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientHistory)
admin.site.register(PatientHistoryFiles)
