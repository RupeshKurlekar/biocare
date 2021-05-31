from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from patient.models import Patient
from master.models import BodyPart, BodyPartView, Priority, ReportStatus, TicketStatus
from radiologist.models import RadiologistReportMap
from .models import Report, ReportFiles, Tickets
from .serializers import ReportSerializers, ReportFilesSerializers, TicketsSerializers, ReportsListSerializer,ReportsDetailSerializer
import logging
from technician.decorator import isuserisLoggedIn
from radiologist.models import Radiologist
logger = logging.getLogger()


# Create your views here.
class ReportDetailsView(APIView):

    def get(self, request,id):
        """
        Get all reports
        """
        try:
            serializer = ReportsDetailSerializer(Report.objects.get(id=id))
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)


class ReportView(APIView):

    def get(self, request):
        """
        Get all reports
        """
        try:
            serializer = ReportsListSerializer(Report.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save reports data
        """
        try:
            
            if request.data['RP_PRIORITY'] == "":
                return JsonResponse({'error': "PLease select Priority"}, status=500)
            
            if request.data['PATIENT'] == "":
                return JsonResponse({'error': "PLease select Patient"}, status=500)
            else:
                if request.data['RADIOLOGIST_TYPE']=="1":
                    report_files_list=[]
                    report_files=[]
                    documents=request.FILES.getlist('RP_FILE')
                    body_parts=request.data.getlist('BODY_PART')
                    body_parts_views=request.data.getlist('BODY_PART_VIEW')
                    print(documents)
                    for i in range(len(documents)):
                        report_files_list.append({"RP_FILE":documents[i],"BODY_PART":body_parts[i],"BODY_PART_VIEW":body_parts_views[i]})
                        report_files.append({"RP_FILE":documents[i]})
                    report_files_serializer= ReportFilesSerializers(data=report_files,many=True)
                    report_serializer = ReportSerializers(data=request.data)

                    if report_serializer.is_valid(raise_exception=True) and report_files_serializer.is_valid(raise_exception=True):
                        if Report.objects.exists():
                            ID = Report.objects.last()
                            RP_ID = 'RPT_' + str(ID.id + 1)
                        else:
                            RP_ID = 'RPT_1'
                        report_serializer.validated_data['RP_ID'] = RP_ID

                    # report_serializer.validated_data['RP_DATE'] = request.data['RP_DATE']
                    # report_serializer.validated_data['RP_TIME'] = request.data['RP_TIME']
                        report_serializer.validated_data['RP_PRIORITY'] = Priority.objects.get(
                            id=request.data['RP_PRIORITY'])
                        report_serializer.validated_data['RP_REMARKS'] = request.data['RP_REMARKS']
                        report_serializer.validated_data['PATIENT'] = Patient.objects.get(
                            id=request.data['PATIENT'])

                        report=report_serializer.save()
                        print('report_files_list',report_files_list)
                        for j in range(len(report_files_list)):

                            ReportFiles.objects.create(RP_FILE=report_files_list[j]['RP_FILE'],BODY_PART=BodyPart.objects.get(id=report_files_list[j]['BODY_PART']),BODY_PART_VIEW=BodyPartView.objects.get(id=report_files_list[j]['BODY_PART_VIEW']),REPORT=report)
                        if RadiologistReportMap.objects.exists():
                            ID = RadiologistReportMap.objects.last()
                            RDLG_RPT_ID = 'RDLGRPID_' + str(ID.id + 1)
                        else:
                            RDLG_RPT_ID = 'RDLGRPID_1'
                        RadiologistReportMap.objects.create(RDLG_RPT_ID=RDLG_RPT_ID,RP_STATUS=ReportStatus.objects.get(id="2"),FINDINGS=""
                                ,IMPRESSIONS="",REPORT=report,RADIOLOGIST=Radiologist.objects.get(id=request.data['RADIOLOGIST']))

                        return JsonResponse({"message": "created successfully"}, status=200)
                    else:
                        return JsonResponse({"message": report_serializer.errors}, status=500)
                else:
                    if Radiologist.objects.filter(RDLG_TYPE="2").exists():
                        report_files_list=[]
                        documents=request.FILES.getlist('RP_FILE')
                        body_parts=request.data.getlist('BODY_PART')
                        body_parts_views=request.data.getlist('BODY_PART_VIEW')
                        for i in range(len(documents)):
                            report_files_list.append({"RP_FILE":documents[i],"BODY_PART":body_parts[i],"BODY_PART_VIEW":body_parts_views[i]})
                
                        report_files_serializer= ReportFilesSerializers(data=report_files_list,many=True)
                        report_serializer = ReportSerializers(data=request.data)

                        if report_serializer.is_valid() and report_files_serializer.is_valid():
                            if Report.objects.exists():
                                ID = Report.objects.last()
                                RP_ID = 'RPT_' + str(ID.id + 1)
                            else:
                                RP_ID = 'RPT_1'
                            report_serializer.validated_data['RP_ID'] = RP_ID
                            report_serializer.validated_data['RP_PRIORITY'] = Priority.objects.get(
                            id=request.data['RP_PRIORITY'])
                            report_serializer.validated_data['RP_REMARKS'] = request.data['RP_REMARKS']
                            report_serializer.validated_data['PATIENT'] = Patient.objects.get(
                                id=request.data['PATIENT'])

                            report=report_serializer.save()
                            print('report_files_list',report_files_list)
                            for j in range(len(report_files_list)):

                           
                                ReportFiles.objects.create(RP_FILE=report_files_list[j]['RP_FILE'],BODY_PART=BodyPart.objects.get(id=report_files_list[j]['BODY_PART']),BODY_PART_VIEW=BodyPartView.objects.get(id=report_files_list[j]['BODY_PART_VIEW']),REPORT=report)
                            biocare_radiologist_list=[]
                            radiologist_queryset=Radiologist.object.filter(RDLG_TYPE="2")

                            for k in range(len(radiologist_queryset)):
                                if RadiologistReportMap.objects.exists():
                                    ID = RadiologistReportMap.objects.last()
                                    RDLG_RPT_ID = 'RDLGRPID_' + str(ID.id + 1)
                                else:
                                    RDLG_RPT_ID = 'RDLGRPID_1'

                                RadiologistReportMap.objects.create(RDLG_RPT_ID=RDLG_RPT_ID,RP_STATUS=ReportStatus.objects.get(id="2"),FINDINGS=""
                                ,IMPRESSIONS="",REPORT=report,RADIOLOGIST=radiologist_queryset[k].id)

                            return JsonResponse({"message": "created successfully"}, status=200)
                        else:
                            return JsonResponse({"message": report_serializer.errors}, status=500)
                    else:
                        return JsonResponse({"message": "Biocare radiologist are not present select other radiologist"}, status=500)


        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class ReportFilesView(APIView):

    def get(self, request):
        """
        Get all reports_file
        """
        try:
            serializer = ReportFilesSerializers(ReportFiles.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save reports_file data
        """
        try:

            if request.data['RP_FILE'] == "":
                return JsonResponse({'error': "PLease enter Remarks"}, status=500)
            if request.data['Report'] == "":
                return JsonResponse({'error': "PLease select Report"}, status=500)
            else:
                reportf_serializer = ReportFilesSerializers(data=request.data)

            if reportf_serializer.is_valid():
                if ReportFiles.objects.exists():
                    ID = ReportFiles.objects.last()
                    RP_FILE_ID = 'RPT_' + str(ID.id + 1)
                else:
                    RP_FILE_ID = 'RPT_1'
                reportf_serializer.validated_data['RP_FILE_ID'] = RP_FILE_ID
                reportf_serializer.validated_data['RP_FILE'] = request.FILES['RP_FILE']
                reportf_serializer.validated_data['Report'] = Report.objects.get(
                        id=request.data['Report'])

                reportf_serializer.save()

                return JsonResponse({"message": "created successfully"}, status=200)
            else:
                return JsonResponse({"message": reportf_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class TicketsView(APIView):

    def get(self, request):
        """
        Get all Tickets
        """
        try:
            serializer = TicketsSerializers(Tickets.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save Tickets data
        """
        try:

            if request.data['TKT_STATUS'] == "":
                return JsonResponse({'error': "PLease enter Status"}, status=500)
            # if request.data['TKT_DATE'] == "":
            #     return JsonResponse({'error': "PLease enter Date"}, status=500)
            # if request.data['TKT_TIME'] == "":
            #     return JsonResponse({'error': "PLease enter Time"}, status=500)
            if request.data['PATIENT'] == "":
                return JsonResponse({'error': "PLease select Patient"}, status=500)
            if request.data['REPORT'] == "":
                return JsonResponse({'error': "PLease enter Remarks"}, status=500)
            if request.data['TKT_REMARKS'] == "":
                return JsonResponse({'error': "PLease enter Remarks"}, status=500)
            else:
                tickets_serializer = TicketsSerializers(data=request.data)

            if tickets_serializer.is_valid():
                if Tickets.objects.exists():
                    ID = Tickets.objects.last()
                    TKT_ID = 'TKT_' + str(ID.id + 1)
                else:
                    TKT_ID = 'TKT_1'
                tickets_serializer.validated_data['TKT_ID'] = TKT_ID

                tickets_serializer.validated_data['TKT_STATUS'] = TicketStatus.objects.get(
                        id=request.data['TKT_STATUS'])
                # tickets_serializer.validated_data['TKT_DATE'] = request.data['TKT_DATE']
                # tickets_serializer.validated_data['TKT_TIME'] = request.data['TKT_TIME']
                tickets_serializer.validated_data['PATIENT'] = Patient.objects.get(
                        id=request.data['PATIENT'])
                tickets_serializer.validated_data['REPORT'] = Report.objects.get(
                        id=request.data['REPORT'])
                tickets_serializer.validated_data['TKT_REMARKS'] = request.data['TKT_REMARKS']

                tickets_serializer.save()

                return JsonResponse({"message": "created successfully"}, status=200)
            else:
                return JsonResponse({"message": tickets_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class ReportsPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,type):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if type== request.session['type']:
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'reports.html',{"is_authenticated":is_authenticated,"type":type})

class AddReportsPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session:
            is_authenticated=request.session['is_authenticated']
            return render(request, 'add_report.html',{"is_authenticated":is_authenticated})

class ReportDetailsPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,id):

        is_authenticated=False
        if "is_authenticated" in request.session:
            is_authenticated=request.session['is_authenticated']
            return render(request, 'view_report.html',{"is_authenticated":is_authenticated})

class EditReportsPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,id):

        is_authenticated=False
        if "is_authenticated" in request.session:
            is_authenticated=request.session['is_authenticated']
            return render(request, 'edit_report.html',{"is_authenticated":is_authenticated})