from django.contrib import admin
from .models import Report, ReportFiles, Tickets

# Register your models here.
admin.site.register(Report)
admin.site.register(ReportFiles)
admin.site.register(Tickets)


