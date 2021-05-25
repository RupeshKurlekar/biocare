from django.db import models
from reports.models import Report
from technician.models import Technician
from django.core.validators import RegexValidator
from master.models import ReportStatus

name_regex = RegexValidator(regex=r'^[a-zA-Z ]+$', message="Please enter valid name")


# Create your models here.
class Radiologist(models.Model):
    RDLG_ID = models.CharField(max_length=255, blank=True)
    RDLG_REG_NO = models.CharField(max_length=255, blank=True)
    RDLG_NAME = models.CharField(validators=[name_regex], max_length=255)
    RDLG_TYPE = models.CharField(max_length=255)
    TECHNICIAN = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=False)  # fk
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Radiologist'

    def __str__(self):
        return self.RDLG_NAME


class RadiologistReportMap(models.Model):
    RDLG_RPT_ID = models.CharField(max_length=255, blank=True)
    RP_STATUS = models.ForeignKey(ReportStatus, on_delete=models.CASCADE, blank=False)
    FINDINGS = models.TextField(max_length=255)
    IMPRESSIONS = models.TextField(max_length=255)
    RADIOLOGIST = models.ForeignKey(Radiologist, on_delete=models.CASCADE, blank=False)  # fk
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)  # fk
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Radiologist Report Map'

    def __str__(self):
        return self.RDLG_RPT_ID


class RadiologistReportFiles(models.Model):
    RDLG_RPT_FILE_ID = models.CharField(max_length=255, blank=True)
    RDLG_RPT_FILE = models.ImageField(upload_to="radiologist_report", max_length=255)
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)  # fk
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Radiologist Report Files'

    def __str__(self):
        return self.RDLG_RPT_FILE


class RadiologistPmt(models.Model):
    RDLG_PMT_ID = models.CharField(max_length=255, blank=True)
    RDLG_PMT_AMT = models.CharField(max_length=255)
    RADIOLOGIST = models.ForeignKey(Radiologist, on_delete=models.CASCADE, blank=False)  # fk
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Radiologist Payment'

    def __str__(self):
        return self.RDLG_PMT_ID
