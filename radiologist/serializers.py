from rest_framework import serializers
from .models import Radiologist, RadiologistReportMap, RadiologistReportFiles, RadiologistPmt,RadiologistPriority


class RadiologistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Radiologist
        exclude=['RDLG_REG_NO']


class RadiologistReportMapSerializers(serializers.ModelSerializer):
    class Meta:
        model = RadiologistReportMap
        fields = '__all__'


class RadiologistReportFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = RadiologistReportFiles
        fields = '__all__'


class RadiologistPmtSerializers(serializers.ModelSerializer):
    class Meta:
        model = RadiologistPmt
        fields = '__all__'

class RadiologistPrioritySerializers(serializers.ModelSerializer):
    class Meta:
        model = RadiologistPriority
        fields = '__all__'
