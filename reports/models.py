from django.db import models
from patient.models import Patient
from master.models import Priority, TicketStatus, BodyPart, BodyPartView
#import magic
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError

# Create your models here.

def validate_image(value):
    file=value.file
    # file_type=magic.from_file(value.file, mime=True)
    initial_pos = file.tell()
    file.seek(0)
    mime_type = magic.from_buffer(file.read(1024), mime=True)
    file.seek(initial_pos)
    print(mime_type)
    if mime_type !="image/jpeg" and mime_type != "application/dicom" and mime_type != "image/png":
        raise ValidationError("Enter valid image format")



    # image_height = image_dimension[1]
    # image_width = image_dimension[0]
    # if image_height != 400 or image_width != 400:
    #     raise ValidationError("Height or Width is larger than what is allowed. Please upload image in  400 X 400 pixels")


class Report(models.Model):
    RP_ID = models.CharField(max_length=255, blank=True)
    RP_REG_NO = models.CharField(max_length=255, blank=True)
    RP_DATE = models.DateTimeField(auto_now=True)  # Date
    RP_PRIORITY = models.ForeignKey(Priority, on_delete=models.CASCADE, blank=False)  # fk
    RP_REMARKS = models.TextField(max_length=255,blank=True)
    PATIENT = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)  # fk
    CREATED_DATE = models.DateTimeField(auto_now=True)

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
    TKT_STATUS = models.ForeignKey(TicketStatus, on_delete=models.CASCADE, blank=False)
    TKT_DATE = models.DateTimeField(auto_now=True)  # date
    TKT_TIME = models.DateTimeField(auto_now=True)  # time
    PATIENT = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=False)  # fk
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    TKT_REMARKS = models.TextField(max_length=255)
    CREATED_DATE = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Tickets'

    def __str__(self):
        return self.TKT_ID


class ReportRadiologist(models.Model):
    REPORT = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    RADIOLOGIST=models.ManyToManyField("radiologist.Radiologist",blank=True)


    class Meta:
        db_table = 'Report Radiologist'

    

