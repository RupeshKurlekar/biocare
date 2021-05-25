from django.contrib import admin
from .models import Radiologist, RadiologistPmt, RadiologistReportFiles, RadiologistReportMap, RadiologistPriority


# Register your models here.

class RadiologistReportMapAdmin(admin.StackedInline):
    model = RadiologistReportMap


admin.site.register(Radiologist)
admin.site.register(RadiologistPmt)
admin.site.register(RadiologistReportFiles)
admin.site.register(RadiologistReportMap)
admin.site.register(RadiologistPriority)