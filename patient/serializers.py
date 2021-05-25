from rest_framework import serializers
from .models import Patient, PatientHistory, PatientHistoryFiles


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude=['PT_REG_NO']


class PatientHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'


class PatientHistoryFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientHistoryFiles
        fields = '__all__'
