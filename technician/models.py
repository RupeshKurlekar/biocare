from django.core.validators import RegexValidator
from django.db import models

name_regex = RegexValidator(regex=r'^[a-zA-Z ]+$', message="Please enter valid name")


class Technician(models.Model):
    TECH_ID = models.CharField(max_length=255)
    TECH_NAME = models.CharField(validators=[name_regex], max_length=255)
    TECH_MOB = models.CharField(max_length=12)
    TECH_EMAIL = models.EmailField(max_length=255)
    TECH_PASSWORD = models.CharField(max_length=255)
    TECH_IMG = models.ImageField(upload_to="technician_profile_pic")  # image
    TECH_ADDRESS = models.TextField(max_length=255)
    TIME = models.DateTimeField(auto_now=True)
    TECH_STATUS = models.CharField(max_length=50, default='Inactive')

    class Meta:
        db_table = 'Technician'

    def __str__(self):
        return self.TECH_NAME

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class TechnicianLogin(models.Model):
    TECHNICIAN = models.ForeignKey(Technician, on_delete=models.CASCADE, null=False, blank=False)
    SESSION_ID = models.CharField(max_length=255, blank=False, null=False)
    LOGIN_DATETIME = models.DateTimeField(blank=False, null=False)
    LOGOUT_DATETIME = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Technician Login'

    def __str__(self):
        return self.TECHNICIAN
