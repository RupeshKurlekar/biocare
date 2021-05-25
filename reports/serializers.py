from rest_framework import serializers
from .models import Report, ReportFiles, Tickets


class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude=['RP_REG_NO']


class ReportFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportFiles
        fields = '__all__'


class TicketsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        exclude=['TKT_REG_NO']
