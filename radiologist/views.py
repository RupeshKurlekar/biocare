from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from technician.models import Technician
from master.models import ReportStatus
from reports.models import Report
from .models import RadiologistPmt, RadiologistReportFiles, RadiologistReportMap, Radiologist
from .serializers import RadiologistSerializers, RadiologistReportMapSerializers, RadiologistReportFilesSerializers, \
    RadiologistPmtSerializers
import logging
logger = logging.getLogger()


# Create your views here.
class RadiologistView(APIView):

    def get(self, request):
        """
        Get all Radiologist
        """
        try:
            serializer = RadiologistSerializers(Radiologist.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save Radiologist data
        """
        try:

            if request.data['RDLG_NAME'] == "":
                return JsonResponse({'error': "PLease enter name "}, status=500)
            if request.data['RDLG_TYPE'] == "":
                return JsonResponse({'error': "PLease enter type"}, status=500)
            if request.data['TECHNICIAN'] == "":
                return JsonResponse({'error': "PLease select Doctor"}, status=500)
            else:
                radiologist_serializer = RadiologistSerializers(data=request.data)

                if radiologist_serializer.is_valid():
                    if Radiologist.objects.exists():
                        ID = Radiologist.objects.last()
                        RDLG_ID = 'RDLG_' + str(ID.id + 1)
                    else:
                        RDLG_ID = 'RDLG_1'
                    radiologist_serializer.validated_data['RDLG_ID'] = RDLG_ID

                    radiologist_serializer.validated_data['RDLG_NAME'] = request.data['RDLG_NAME']
                    radiologist_serializer.validated_data['RDLG_TYPE'] = request.data['RDLG_TYPE']
                    radiologist_serializer.validated_data['TECHNICIAN'] = Technician.objects.get(
                        id=request.data['TECHNICIAN'])

                    radiologist_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": radiologist_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class RadiologistPmtView(APIView):

    def get(self, request):
        """
        Get all Radiologist_Payment
        """
        try:
            serializer = RadiologistPmtSerializers(RadiologistPmt.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save Radiologist data
        """
        try:
            if request.data['RDLG_PMT_AMT'] == "":
                return JsonResponse({'error': "PLease enter name "}, status=500)
            if request.data['RADIOLOGIST'] == "":
                return JsonResponse({'error': "PLease enter type"}, status=500)

            else:
                radiologistpmt_serializer = RadiologistPmtSerializers(data=request.data)

                if radiologistpmt_serializer.is_valid():
                    if RadiologistPmt.objects.exists():
                        ID = RadiologistPmt.objects.last()
                        RDLG_PMT_ID = 'RDLGPMT_' + str(ID.id + 1)
                    else:
                        RDLG_PMT_ID = 'RDLGPMT_1'
                    radiologistpmt_serializer.validated_data['RDLG_PMT_ID'] = RDLG_PMT_ID
                    radiologistpmt_serializer.validated_data['RDLG_PMT_AMT'] = request.data['RDLG_PMT_AMT']
                    radiologistpmt_serializer.validated_data['RADIOLOGIST'] = Radiologist.objects.get(
                        id=request.data['RADIOLOGIST'])

                    radiologistpmt_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": radiologistpmt_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class RadiologistReportMapView(APIView):

    def get(self, request):
        """
        Get all sellers
        """
        try:
            serializer = RadiologistReportMapSerializers(RadiologistReportMap.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save seller data
        """
        try:
            if request.data['RP_STATUS'] == "":
                return JsonResponse({'error': "PLease enter name "}, status=500)
            if request.data['FINDINGS'] == "":
                return JsonResponse({'error': "PLease enter name "}, status=500)
            if request.data['IMPRESSIONS'] == "":
                return JsonResponse({'error': "PLease enter name "}, status=500)
            if request.data['RADIOLOGIST'] == "":
                return JsonResponse({'error': "PLease enter type"}, status=500)
            if request.data['REPORT'] == "":
                return JsonResponse({'error': "PLease enter type"}, status=500)

            else:
                radiologistrm_serializer = RadiologistReportMapSerializers(data=request.data)

                if radiologistrm_serializer.is_valid():
                    if RadiologistReportMap.objects.exists():
                        ID = RadiologistReportMap.objects.last()
                        RDLG_RPT_ID = 'RDLGRPID_' + str(ID.id + 1)
                    else:
                        RDLG_RPT_ID = 'RDLGRPID_1'
                    radiologistrm_serializer.validated_data['RDLG_RPT_ID'] = RDLG_RPT_ID
                    radiologistrm_serializer.validated_data['RP_STATUS'] = ReportStatus.objects.get(
                        id=request.data['RP_STATUS'])
                    radiologistrm_serializer.validated_data['FINDINGS'] = request.data['FINDINGS']
                    radiologistrm_serializer.validated_data['IMPRESSIONS'] = request.data['IMPRESSIONS']
                    radiologistrm_serializer.validated_data['RADIOLOGIST'] = Radiologist.objects.get(
                        id=request.data['RADIOLOGIST'])
                    radiologistrm_serializer.validated_data['REPORT'] = Report.objects.get(
                        id=request.data['REPORT'])

                    radiologistrm_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": radiologistrm_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class RadiologistReportFilesView(APIView):

    def get(self, request):
        """
        Get all sellers
        """
        try:
            serializer = RadiologistReportFilesSerializers(RadiologistReportFiles.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save seller data
        """
        try:
            if request.data['RDLG_RPT_FILE'] == "":
                return JsonResponse({'error': "PLease enter name "}, status=500)
            if request.data['REPORT'] == "":
                return JsonResponse({'error': "PLease enter type"}, status=500)

            else:
                radiologistrf_serializer = RadiologistReportFilesSerializers(data=request.data)

                if radiologistrf_serializer.is_valid():
                    if RadiologistReportMap.objects.exists():
                        ID = RadiologistReportMap.objects.last()
                        RDLG_RPT_FILE_ID = 'RDLGRPFID_' + str(ID.id + 1)
                    else:
                        RDLG_RPT_FILE_ID = 'RDLGRPFID_1'
                    radiologistrf_serializer.validated_data['RDLG_RPT_FILE_ID'] = RDLG_RPT_FILE_ID
                    radiologistrf_serializer.validated_data['RDLG_RPT_FILE'] = request.FILES['RDLG_RPT_FILE']
                    radiologistrf_serializer.validated_data['REPORT'] = Report.objects.get(
                        id=request.data['REPORT'])

                    radiologistrf_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": radiologistrf_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)
