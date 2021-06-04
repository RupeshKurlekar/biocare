from django.db import models
from patient.models import Patient
from master.models import Priority, TicketStatus, BodyPart, BodyPartView
import magic
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError

# Create your models here.

def validate_image(value):
    file=value.file
    initial_pos = file.tell()
    file.seek(0)
    mime_type = magic.from_buffer(file.read(1024), mime=True)
    file.seek(initial_pos)
    if mime_type !="image/jpeg" and mime_type != "application/dicom" and mime_type != "image/png":
        raise ValidationError("Enter valid image format",code=412)





class Report(models.Model):
    RP_ID = models.CharField(max_length=255, blank=True)
    RP_REG_NO = models.CharField(max_length=255, blank=True)
    RP_DATE = models.DateTimeField(auto_now=True)  # Date
    RP_PRIORITY = models.ForeignKey(Priority, on_delete=models.CASCADE, blank=False)  # fk
    RP_REMARKS = models.TextField(max_length=255,blank=True)
    PATIENT = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)  # fk
    IS_DELETED=models.BooleanField(default=0,blank=True, null=True)
    CREATED_DATE = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Report'

    def __str__(self):
        return self.RP_ID


class ReportFiles(models.Model):
    RP_FILE = models.FileField(validators=[validate_image],upload_to="reports")
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    BODY_PART = models.ForeignKey(BodyPart, on_delete=models.CASCADE, blank=False)
    BODY_PART_VIEW = models.ForeignKey(BodyPartView, on_delete=models.CASCADE, blank=False)
    CREATED_DATE = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Report Files'

    def __str__(self):
        return str(self.id)


class Tickets(models.Model):
    TKT_ID = models.CharField(max_length=255, blank=True)
    TKT_REG_NO = models.CharField(max_length=255, blank=True)
    TKT_STATUS = models.CharField(max_length=50, blank=True)
    PATIENT = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)  # fk
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    TKT_REMARKS = models.TextField(max_length=255)
    CREATED_DATE = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Tickets'

    def __str__(self):
        return self.TKT_ID


class TicketRadiologistMap(models.Model):
    TICKET = models.ForeignKey(Tickets, on_delete=models.CASCADE, blank=False)
    RADIOLOGIST=models.ForeignKey("radiologist.Radiologist",blank=False,on_delete=models.CASCADE)
    CREATED_DATE = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Ticket Radiologist Map'

    



