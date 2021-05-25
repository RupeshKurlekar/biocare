from django.db import models
from patient.models import Patient
from master.models import Priority, TicketStatus


# Create your models here.

class Report(models.Model):
    RP_ID = models.CharField(max_length=255, blank=True)
    RP_REG_NO = models.CharField(max_length=255, blank=True)
    RP_DATE = models.DateTimeField(auto_now=True)  # Date
    RP_TIME = models.DateTimeField(auto_now=True)  # Time
    RP_PRIORITY = models.ForeignKey(Priority, on_delete=models.CASCADE, blank=False)  # fk
    RP_REMARKS = models.TextField(max_length=255)
    PATIENT = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)  # fk
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Report'

    def __str__(self):
        return self.RP_ID


class ReportFiles(models.Model):
    RP_FILE_ID = models.CharField(max_length=255, blank=True)
    RP_FILE = models.ImageField(upload_to="reports")
    Report = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Report Files'

    def __str__(self):
        return self.RP_FILE


class Tickets(models.Model):
    TKT_ID = models.CharField(max_length=255, blank=True)
    TKT_REG_NO = models.CharField(max_length=255, blank=True)
    TKT_STATUS = models.ForeignKey(TicketStatus, on_delete=models.CASCADE, blank=False)
    TKT_DATE = models.DateTimeField(auto_now=True)  # date
    TKT_TIME = models.DateTimeField(auto_now=True)  # time
    PATIENT = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)  # fk
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    TKT_REMARKS = models.TextField(max_length=255)
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Tickets'

    def __str__(self):
        return self.TKT_ID
