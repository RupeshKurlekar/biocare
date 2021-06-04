from django.contrib import admin
from .models import Technician, TechnicianLogin,Wallet


# Register your models here.


class TechnicianAdmin(admin.ModelAdmin):
    model = Technician
    exclude = ['TECH_ID', 'TIME']

class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    
    list_display=['TECHNICIAN','WALLET_AMT']


admin.site.register(Technician, TechnicianAdmin)
admin.site.register(Wallet,WalletAdmin)
