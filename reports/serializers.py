from rest_framework import serializers
from .models import Report, ReportFiles, Tickets
from master.models import BodyPart
from radiologist.models import RadiologistReportMap
from radiologist.serializers import RadiologistReportMapSerializers
from dateutil import parser

class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude=['RP_REG_NO']


class ReportFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportFiles
        fields = ['RP_FILE']

class ReportFilesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportFiles
        fields = '__all__'
        depth=1


class TicketsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        exclude=['TKT_REG_NO']

class ReportsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude=['RP_REG_NO']
        depth=1


    def to_representation(self,instance):
        data=super().to_representation(instance)
        if ReportFiles.objects.filter(REPORT=data['id']).exists():
            files_list=ReportFiles.objects.filter(REPORT=data['id'])
            body_parts=[]
            body_part_views=[]
            for i in range(len(files_list)):
                body_parts.append(files_list[i].BODY_PART.NAME)
                body_part_views.append(files_list[i].BODY_PART_VIEW.VIEWS_SIDE)
            data['BODY_PART']=", ".join(map(str, body_parts))
            data['BODY_PART_VIEW']=", ".join(map(str, body_part_views))
        else:
            data['BODY_PART']=""
            data['BODY_PART_VIEW']=""
        if RadiologistReportMap.objects.filter(REPORT=data['id']).exists():
            map_list=RadiologistReportMap.objects.filter(REPORT=data['id'])
            status_list=[]
            for j in range(len(map_list)):
                status_list.append(map_list[j].RP_STATUS)
            if "1" in status_list:
                data['STATUS']="Completed"
            else:
                data['STATUS']="Pending"
            data['RADIOLOGIST_ASSIGNED']=True
        else:
            data['STATUS']="Pending"
            data['RADIOLOGIST_ASSIGNED']=False

        if data['RP_DATE'] :
            dateandtime = parser.parse(data['RP_DATE'])
            data['RP_DATE'] = dateandtime.strftime("%d %b %Y  %I:%M %p")
        return data

class ReportsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude=['RP_REG_NO']
        depth=1


    def to_representation(self,instance):
        data=super().to_representation(instance)
        if ReportFiles.objects.filter(REPORT=data['id']).exists():
            
            data['DOCUMENT']=ReportFilesListSerializers(ReportFiles.objects.filter(REPORT=data['id']),many=True).data

        else:
            data['DOCUMENT']=""
           
        if RadiologistReportMap.objects.filter(REPORT=data['id']).exists():
            map_list=RadiologistReportMap.objects.filter(REPORT=data['id'])
            status_list=[]
            for j in range(len(map_list)):
                status_list.append(map_list[j].RP_STATUS)
            if "1" in status_list:
                data['STATUS']="Completed"
            else:
                data['STATUS']="Pending"
            data['RADIOLOGIST_ASSIGNED']=True
            
        else:
            data['STATUS']="Pending"
            data['RADIOLOGIST_ASSIGNED']=False

        if data['RP_DATE'] :
            dateandtime = parser.parse(data['RP_DATE'])
            data['RP_DATE'] = dateandtime.strftime("%d %b %Y  %I:%M %p")
        return data
