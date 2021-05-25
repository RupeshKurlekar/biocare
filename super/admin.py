from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Super, SuperLogin


# Register your models here.


class SuperAdmin(admin.ModelAdmin):
    model = Super
    exclude = ['SUPER_ID', 'TIME']


admin.site.register(Super, SuperAdmin)