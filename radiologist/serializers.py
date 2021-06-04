from rest_framework import serializers
from .models import Radiologist, RadiologistReportMap, RadiologistReportFiles, RadiologistPmt,RadiologistPriority,TransactionLog


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

class RadiologistReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = RadiologistReportMap
        fields = '__all__'
        depth=2

    def to_representation(self, instance):
        data=super().to_representation(instance)
        if ReportFiles.objects.filter(REPORT=data['REPORT']['id']).exists():
            files_list=ReportFiles.objects.filter(REPORT=data['REPORT']['id'])
            body_parts=[]
            body_part_views=[]
            for i in range(len(files_list)):
                body_parts.append(files_list[i].BODY_PART.NAME)
                body_part_views.append(files_list[i].BODY_PART_VIEW.VIEWS_SIDE)
            data['BODY_PART']=body_parts[0]
            data['BODY_PART_VIEW']=", ".join(map(str, body_part_views))
        else:
            data['BODY_PART']=""
            data['BODY_PART_VIEW']=""
        

        if data['REPORT']['RP_DATE']:
            dateandtime = parser.parse(data['REPORT']['RP_DATE'])
            data['RP_DATE'] = dateandtime.strftime("%d %b %Y  %I:%M %p")
        # data['PATIENT']=PatientSerializers(Patient.objects.get(id=data['REPORT']['PATIENT'])).data
        
        return data

    
class RadiologistReportDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = RadiologistReportMap
        fields = '__all__'
        depth=2

    def to_representation(self, instance):
        data=super().to_representation(instance)
        if ReportFiles.objects.filter(REPORT=data['REPORT']['id']).exists():
            data['REPORT_DOCUMENTS']=ReportFilesListSerializers(ReportFiles.objects.filter(REPORT=data['REPORT']['id']),many=True).data
        else:
            data['REPORT_DOCUMENTS']=""

        if data['REPORT']['RP_DATE']:
            dateandtime = parser.parse(data['REPORT']['RP_DATE'])
            data['RP_DATE'] = dateandtime.strftime("%d %b %Y  %I:%M %p")
        # data['PATIENT']=PatientSerializers(Patient.objects.get(id=data['REPORT']['PATIENT'])).data
        data['RADIOLOGIST']=RadiologistSerializers(Radiologist.objects.get(id=data['RADIOLOGIST']['id'])).data
        return data

class TransactionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLog
        fields = '__all__'

class TransactionLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLog
        fields = '__all__'
        depth=2
