from django.shortcuts import render
from master.models import ReportStatus, Priority, TicketStatus, BodyPart, BodyPartView
from master.serializers import ReportStatusSerializers, PrioritySerializers, TicketStatusSerializers, BodyPartSerializers, BodyPartViewSerializers
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView
import logging

logger = logging.getLogger()

# Create your views here.

class ReportStatusView(APIView):

    def get(self, request):
        """
        Get all Technician
        """
        try:
            serializer = ReportStatusSerializers(ReportStatus.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class PriorityView(APIView):

    def get(self, request):
        """
        Get all Technician
        """
        try:
            serializer = PrioritySerializers(Priority.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class TicketStatusView(APIView):

    def get(self, request):
        """
        Get all Technician
        """
        try:
            serializer = TicketStatusSerializers(TicketStatus.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class BodyParts(APIView):

    def get(self, request):
        """
        Get all Technician
        """
        try:
            serializer = BodyPartSerializers(BodyPart.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class BodyPartViewsView(APIView):

    def get(self, request):
        """
        Get all Technician
        """
        try:
            serializer = BodyPartViewSerializers(BodyPartView.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)
