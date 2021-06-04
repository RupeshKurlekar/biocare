from django.db import models
from reports.models import Report
from technician.models import Technician
from django.core.validators import RegexValidator
from master.models import Priority, ReportStatus

name_regex = RegexValidator(regex=r'^[a-zA-Z ]+$', message="Please enter valid name")


# Create your models here.
class Radiologist(models.Model):
    RDLG_ID = models.CharField(max_length=255, blank=True)
    RDLG_REG_NO = models.CharField(max_length=255, blank=True)
    RDLG_NAME = models.CharField(validators=[name_regex], max_length=255)
    RDLG_MOB_NO = models.CharField(max_length=12)
    RDLG_EMAIL = models.EmailField(max_length=255)
    RDLG_PASSWORD = models.CharField(max_length=255)
    RDLG_IMG = models.ImageField(upload_to="radiologist_profile_pic")  # image
    RDLG_ADDRESS = models.TextField(max_length=255)
    RDLG_AREA = models.TextField(max_length=255)
    RDLG_QUALIFICATION = models.TextField(max_length=100)
    RDLG_EXPERIENCE = models.CharField(max_length=10)
    RDLG_SPECIALITY = models.TextField(max_length=255)
    RDLG_TYPE = models.CharField(max_length=10)
    RDLG_GST = models.CharField(max_length=12)
    TECHNICIAN = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=True,null=True)  # fk
    IS_APPROVED = models.BooleanField(default=False)

    CREATED_AT = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Radiologist'

    def __str__(self):
        return self.RDLG_NAME


class RadiologistReportMap(models.Model):
    RDLG_RPT_ID = models.CharField(max_length=255, blank=True)
    RP_STATUS = models.ForeignKey(ReportStatus, on_delete=models.CASCADE, blank=False)
    FINDINGS = models.TextField()
    IMPRESSIONS = models.TextField()
    RADIOLOGIST = models.ForeignKey(Radiologist, on_delete=models.CASCADE, blank=False)  # fk
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)  # fk
    CREATED_AT = models.DateTimeField(auto_now_add=True)

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
        return self.REPORT.RP_ID


class RadiologistPmt(models.Model):
    RDLG_PMT_ID = models.CharField(max_length=255, blank=True)
    RDLG_PMT_AMT = models.CharField(max_length=255)
    RADIOLOGIST = models.ForeignKey(Radiologist, on_delete=models.CASCADE, blank=False)  # fk
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Radiologist Payment'

    def __str__(self):
        return self.RDLG_PMT_ID


class RadiologistLogin(models.Model):
    RADIOLOGIST = models.ForeignKey(Radiologist, on_delete=models.CASCADE, null=False, blank=False)
    SESSION_ID = models.CharField(max_length=255, blank=False, null=False)
    LOGIN_DATETIME = models.DateTimeField(blank=False, null=False)
    LOGOUT_DATETIME = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Radiologist Login'

    def __str__(self):
        return self.RADIOLOGIST

class RadiologistPriority(models.Model):
    PRIORITY = models.ForeignKey(Priority, on_delete=models.CASCADE, null=False, blank=False)
    RADIOLOGIST = models.ForeignKey(Radiologist, on_delete=models.CASCADE, blank=True,null=True)
    RADIOLOGIST_PRICE = models.CharField(max_length=255)

    class Meta:
        db_table = 'Radiologist Priority'
    
    def __str__(self):
        return self.PRIORITY.NAME


class TransactionLog(models.Model):
    TRANS_ID= models.CharField(max_length=255, blank=True)
    TECHNICIAN = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=True,null=True)
    RADIOLOGIST = models.ForeignKey(Radiologist, on_delete=models.CASCADE, blank=True,null=True)
    AMOUNT=models.CharField(max_length=55)
    REPORTS_COUNT=models.CharField(max_length=55)
    REPORTS_DESCRIPTION=models.TextField()
    REMARK=models.TextField()


    class Meta:
        db_table = 'Transaction Log'
    
    def __str__(self):
        return self.RADIOLOGIST.RDLG_NAME