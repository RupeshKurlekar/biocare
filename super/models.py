from django.core.validators import RegexValidator
from django.db import models

name_regex = RegexValidator(regex=r'^[a-zA-Z ]+$', message="Please enter valid name")


class Super(models.Model):
    SUPER_ID = models.CharField(max_length=255)
    SUPER_NAME = models.CharField(validators=[name_regex], max_length=255)
    SUPER_MOB = models.CharField(max_length=12)
    SUPER_EMAIL = models.EmailField(max_length=255)
    SUPER_PASSWORD = models.CharField(max_length=255)
    TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Super'

    def __str__(self):
        return self.SUPER_NAME

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class SuperLogin(models.Model):
    SUPER = models.ForeignKey(Super, on_delete=models.CASCADE, null=False, blank=False)
    SESSION_ID = models.CharField(max_length=255, blank=False, null=False)
    LOGIN_DATETIME = models.DateTimeField(blank=False, null=False)
    LOGOUT_DATETIME = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Super Login'

    def __str__(self):
        return self.SUPER