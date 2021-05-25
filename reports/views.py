from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from patient.models import Patient
from master.models import Priority, TicketStatus
from .models import Report, ReportFiles, Tickets
from .serializers import ReportSerializers, ReportFilesSerializers, TicketsSerializers
import logging

logger = logging.getLogger()


# Create your views here.
class ReportDetailsView(APIView):

    def get(self, request,id):
        """
        Get all reports
        """
        try:
            serializer = ReportSerializers(Report.objects.get(id=id))
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
            serializer = ReportSerializers(Report.objects.all(), many=True)
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

            # if request.data['RP_DATE'] == "":
            #     return JsonResponse({'error': "PLease enter Date"}, status=500)
            # if request.data['RP_TIME'] == "":
            #     return JsonResponse({'error': "PLease enter Time"}, status=500)

            if request.data['RP_PRIORITY'] == "":
                return JsonResponse({'error': "PLease select Priority"}, status=500)
            if request.data['RP_REMARKS'] == "":
                return JsonResponse({'error': "PLease enter Remarks"}, status=500)
            if request.data['PATIENT'] == "":
                return JsonResponse({'error': "PLease select Patient"}, status=500)
            else:
                report_serializer = ReportSerializers(data=request.data)

                if report_serializer.is_valid():
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

                    report_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": report_serializer.errors}, status=500)

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
