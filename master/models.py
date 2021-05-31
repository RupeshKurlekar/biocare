from django.db import models


# Create your models here.
class ReportStatus(models.Model):
    STATUS = models.CharField(max_length=55)
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.STATUS

    class Meta:
        verbose_name_plural='Report Status'


class Priority(models.Model):
    PRIORITY = models.CharField(max_length=55)
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PRIORITY
    
    class Meta:
        verbose_name_plural='Priorities'


class TicketStatus(models.Model):
    STATUS = models.CharField(max_length=55)
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.STATUS
    
    class Meta:
        verbose_name_plural='Ticket Status'

class BodyPart(models.Model):
    NAME = models.CharField(max_length=255)
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NAME
    
    class Meta:
        verbose_name_plural='Body Parts'
    

class BodyPartView(models.Model):
    VIEWS_SIDE = models.CharField(max_length=255)
    CREATED_AT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.VIEWS_SIDE

    class Meta:
        verbose_name_plural='Body Parts Views'
