from django.db import models
from django.core.validators import RegexValidator
from technician.models import Technician

name_regex = RegexValidator(regex=r'^[a-zA-Z ]+$', message="Please enter valid name")


# Create your models here.
class Patient(models.Model):
    PT_ID = models.CharField(max_length=255, blank=True)
    PT_REG_NO = models.CharField(max_length=255)
    PT_NAME = models.CharField(validators=[name_regex], max_length=255)
    PT_GENDER = models.CharField(max_length=20)
    PT_AGE = models.CharField(max_length=255)
    PT_MOB = models.CharField(max_length=255)
    TECHNICIAN = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=False)  # fk
    IS_DELETED=models.BooleanField(default=0,blank=True, null=True)
    CREATED_DATE = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Patient'

    def __str__(self):
        return self.PT_NAME


class PatientHistory(models.Model):
    PT_HSTY_ID = models.CharField(max_length=255, blank=True)
    IS_SENT = models.BooleanField(default=False)
    RP_REMARKS = models.TextField()
    PATIENT = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)  # fk
    CREATED_DATE = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Patient History'

    def __str__(self):
        return self.PT_HSTY_ID


class PatientHistoryFiles(models.Model):
    PT_HSTY_FILE_ID = models.CharField(max_length=255, blank=True)
    PT_HSTY_FILE = models.ImageField(upload_to="patient_history_files", max_length=255)
    PatientHistory = models.ForeignKey(PatientHistory, on_delete=models.CASCADE, blank=False)  # this
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Patient History Files'

    def __str__(self):
        return self.PT_HSTY_FILE
