from rest_framework import serializers
from .models import Technician,TechnicianPriority,Wallet


class TechnicianListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Technician
        exclude = ['TECH_PASSWORD']


class TechnicianSerializers(serializers.ModelSerializer):
    class Meta:
        model = Technician
        exclude = ['TECH_ID']

class TechnicianPrioritySerializers(serializers.ModelSerializer):
    class Meta:
        model = TechnicianPriority
        fields = "__all__"

class WalletSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields="__all__"
