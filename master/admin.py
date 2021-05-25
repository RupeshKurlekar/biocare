from django.contrib import admin
from .models import TicketStatus, ReportStatus, Priority

# Register your models here.

admin.site.register(ReportStatus)
admin.site.register(TicketStatus)
admin.site.register(Priority)
