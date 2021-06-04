from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Patient, PatientHistoryFiles, PatientHistory
from .serializers import PatientSerializers, PatientHistorySerializers, PatientHistoryFilesSerializers,PatientUpdateSerializers
import logging
from random import randint
from django.views.generic import TemplateView
from technician.decorator import isuserisLoggedIn

logger = logging.getLogger()

from technician.models import Technician
from django.urls import reverse_lazy


# Create your views here.
class PatientDetailsView(APIView):

    def get(self, request, id):
        """
        Get all patient
        """
        try:
            serializer = PatientSerializers(Patient.objects.get(id=id))
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)


class PatientView(APIView):

    def get(self, request):
        """
        Get all patient
        """
        try:
            type = request.GET.get('type') 
            tech_id = request.GET.get('tech_id') 
            if type=='technician':
                serializer = PatientSerializers(Patient.objects.filter(TECHNICIAN=tech_id).filter(IS_DELETED=False), many=True)
                return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
            elif type=='super':
                serializer = PatientSerializers(Patient.objects.filter(IS_DELETED=False), many=True)
                return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
            
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save patient data
        """
        try:

            if request.data['PT_NAME'] == "":
                return JsonResponse({'error': "PLease enter Name"}, status=500)
            if request.data['PT_GENDER'] == "":
                return JsonResponse({'error': "PLease enter Gender"}, status=500)
            if request.data['PT_AGE'] == "":
                return JsonResponse({'error': "PLease enter Age"}, status=500)
            if request.data['PT_MOB'] == "":
                return JsonResponse({'error': "PLease enter Mobile Number"}, status=500)
            if request.data['TECHNICIAN'] == "":
                return JsonResponse({'error': "PLease select Doctor"}, status=500)

            else:

                patient_serializer = PatientSerializers(data=request.data)

                if patient_serializer.is_valid():
                    if Patient.objects.exists():
                        ID = Patient.objects.last()
                        PT_ID = 'PT_' + str(ID.id + 1)
                    else:
                        PT_ID = 'PT_1'

                    patient_serializer.validated_data['PT_ID'] = PT_ID
                    patient_serializer.validated_data['PT_NAME'] = request.data['PT_NAME']
                    patient_serializer.validated_data['PT_GENDER'] = request.data['PT_GENDER']
                    patient_serializer.validated_data['PT_AGE'] = request.data['PT_AGE']
                    patient_serializer.validated_data['PT_MOB'] = request.data['PT_MOB']
                    patient_serializer.validated_data['TECHNICIAN'] = Technician.objects.get(
                        id=request.data['TECHNICIAN'])

                    patient_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": patient_serializer.errors}, status=500)
        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)

    


class PatientHistoryDetailsView(APIView):

    def get(self, request, id):
        """
        Get all patients
        """
        try:
            serializer = PatientHistorySerializers(PatientHistory.objects.get(pk=id))
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)


class PatientHistoryView(APIView):

    def get(self, request):
        """
        Get all patients
        """
        try:
            serializer = PatientHistorySerializers(PatientHistory.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save patient data
        """
        try:
            
           
            if request.data['PATIENT'] == "":
                return JsonResponse({'error': "PLease select patient"}, status=500)

            else:
                patienthistory_serializer = PatientHistorySerializers(data=request.data)

                if patienthistory_serializer.is_valid():
                    if PatientHistory.objects.exists():
                        ID = PatientHistory.objects.last()
                        PT_HSTY_ID = 'PTHS_' + str(ID.id + 1)
                    else:
                        PT_HSTY_ID = 'PTHS_1'
                    patienthistory_serializer.validated_data['PT_HSTY_ID'] = PT_HSTY_ID
                    patienthistory_serializer.validated_data['IS_SENT'] = False
                    patienthistory_serializer.validated_data['RP_REMARKS'] = request.data['RP_REMARKS']
                    patienthistory_serializer.validated_data['PATIENT'] = Patient.objects.get(
                        id=request.data['PATIENT'])

                    patienthistory_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": patienthistory_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class PatientHistoryFilesView(APIView):

    def get(self, request):
        """
        Get all patients
        """
        try:
            serializer = PatientHistoryFilesSerializers(PatientHistoryFiles.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save patient data
        """
        try:
            if request.data['PT_HSTY_FILE'] == "":
                return JsonResponse({'error': "PLease upload file"}, status=500)
            if request.data['PatientHistory'] == "":
                return JsonResponse({'error': "PLease enter remarks"}, status=500)

            else:
                patienthistoryfile_serializer = PatientHistoryFilesSerializers(data=request.data)

                if patienthistoryfile_serializer.is_valid():
                    if PatientHistoryFiles.objects.exists():
                        ID = PatientHistoryFiles.objects.last()
                        PT_HSTY_ID = 'PTHSF_' + str(ID.id + 1)
                    else:
                        PT_HSTY_ID = 'PTHSF_1'
                    patienthistoryfile_serializer.validated_data['PT_HSTY_FILE_ID'] = PT_HSTY_ID
                    patienthistoryfile_serializer.validated_data['PT_HSTY_FILE'] = request.FILES['PT_HSTY_FILE']
                    patienthistoryfile_serializer.validated_data['PatientHistory'] = PatientHistory.objects.get(
                        id=request.data['PatientHistory'])

                    patienthistoryfile_serializer.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": patienthistoryfile_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class PatientsPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,type):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if type== request.session['type']:
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'patients.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))

class PatientUpdateView(APIView):
    def post(self, request):
        """
        UPDATE patient data
        """
        try:

            if request.data['PT_NAME'] == "":
                return JsonResponse({'error': "PLease enter Name"}, status=500)
            if request.data['PT_GENDER'] == "":
                return JsonResponse({'error': "PLease enter Gender"}, status=500)
            if request.data['PT_AGE'] == "":
                return JsonResponse({'error': "PLease enter Age"}, status=500)
            if request.data['PT_MOB'] == "":
                return JsonResponse({'error': "PLease enter Mobile Number"}, status=500)

            else:

                patient_serializer = PatientUpdateSerializers(data=request.data)

                if patient_serializer.is_valid():
                    
                    patient=Patient.objects.get(id= request.data['id'])
                    patient.PT_NAME = request.data['PT_NAME']
                    patient.PT_GENDER = request.data['PT_GENDER']
                    patient.PT_AGE = request.data['PT_AGE']
                    patient.PT_MOB = request.data['PT_MOB']
                    patient.save()


                    return JsonResponse({"message": "updated successfully"}, status=200)
                else:
                    return JsonResponse({"message": patient_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)

class DeletePatientView(APIView):
    def get(self,request,id):
            
        """
        delete patient
        """
        try:
            patient=Patient.objects.get(id=id)
            patient.IS_DELETED=True
            patient.save()
            return JsonResponse({"message": "patient deleted successfully"}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class RadiologistPatientHistoryPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if request.session['type']=="radiologist":
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'radiologist_send_patient_history.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))
