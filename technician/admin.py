from django.contrib import admin
from .models import Technician, TechnicianLogin


# Register your models here.


class TechnicianAdmin(admin.ModelAdmin):
    model = Technician
    exclude = ['TECH_ID', 'TIME']


admin.site.register(Technician, TechnicianAdmin)
