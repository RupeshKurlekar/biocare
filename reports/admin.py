from django.contrib import admin
from .models import Report, ReportFiles, Tickets


class ReportAdmin(admin.ModelAdmin):
    model=Report
    list_display=['RP_ID','RP_DATE','RP_PRIORITY','PATIENT','CREATED_DATE']
# Register your models here.
admin.site.register(Report,ReportAdmin)
admin.site.register(ReportFiles)
admin.site.register(Tickets)


