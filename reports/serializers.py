from rest_framework import serializers

from .models import Report, ReportFiles, Tickets, TicketRadiologistMap
from master.models import BodyPart
from radiologist.models import Radiologist, RadiologistReportMap
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
            data['BODY_PART']=body_parts[0]
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

class TicketRadiologistMapSerializers(serializers.ModelSerializer):
    class Meta:
        model = TicketRadiologistMap
        fields = '__all__'
        depth=2

    def to_representation(self, instance):
        data=super().to_representation(instance)
        if ReportFiles.objects.filter(REPORT=data['TICKET']['REPORT']['id']).exists():
            files_list=ReportFiles.objects.filter(REPORT=data['TICKET']['REPORT']['id'])
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
        data['RADIOLOGIST']=Radiologist.objects.get(id=data['RADIOLOGIST']['id']).RDLG_NAME
        
        return data

class ReportsRadiologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude=['RP_REG_NO']
        depth=1
    def to_representation(self,instance):
        data=super().to_representation(instance)
        if Radiologist.objects.filter(REPORT=data['id']).exists():
            files_list=Radiologist.objects.filter(REPORT=data['id'])
            rdlg_name=[]
            for i in range(len(files_list)):
                rdlg_name.append(files_list[i].RDLG_NAME.NAME)
            data['RDLG_NAME']=rdlg_name[0]
        else:
            data['RDLG_NAME']=""
        data['RADIOLOGIST']=Radiologist.objects.get(id=data['RADIOLOGIST']['id']).RDLG_NAME
        if data['RP_DATE'] :
            dateandtime = parser.parse(data['RP_DATE'])
            data['RP_DATE'] = dateandtime.strftime("%d %b %Y  %I:%M %p")
        return data