import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView

from .models import TechnicianLogin, Technician
from .serializers import TechnicianSerializers, TechnicianListSerializers
import logging
from django.urls import reverse_lazy
from django.views.generic import TemplateView
logger = logging.getLogger()


# Create your views here.
class TechnicianView(APIView):

    def get(self, request):
        """
        Get all Technician
        """
        try:
            serializer = TechnicianListSerializers(Technician.objects.filter(TECH_STATUS='Active'), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

    def post(self, request):
        """
        Save Technician data
        """
        try:

            if request.data['TECH_NAME'] == "":
                return JsonResponse({'error': "PLease enter name"}, status=500)
            if request.data['TECH_MOB'] == "":
                return JsonResponse({'error': "PLease enter Mobile Number"}, status=500)
            if request.data['TECH_EMAIL'] == "":
                return JsonResponse({'error': "PLease enter Email"}, status=500)
            if request.data['TECH_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter password"}, status=500)
            if not request.FILES.get('TECH_IMG',False):
                return JsonResponse({'error': "PLease upload image"}, status=500)
            if request.data['TECH_ADDRESS'] == "":
                return JsonResponse({'error': "PLease enter ADDRESS"}, status=500)
            else:
                if Technician.objects.filter(TECH_MOB=request.data['TECH_MOB']).exists():
                    return JsonResponse({'error': "Mobile Number already exists"}, status=500)
                else:
                    technician_serializer = TechnicianSerializers(data=request.data)

                    if technician_serializer.is_valid():
                        if Technician.objects.exists():
                            ID = Technician.objects.last()
                            TECH_ID = 'T_' + str(ID.id + 1)
                        else:
                            TECH_ID = 'T_1'
                        technician_serializer.validated_data['TECH_ID'] = TECH_ID
                        technician_serializer.validated_data['TECH_NAME'] = request.data['TECH_NAME']
                        technician_serializer.validated_data['TECH_MOB'] = request.data['TECH_MOB']
                        technician_serializer.validated_data['TECH_EMAIL'] = request.data['TECH_EMAIL']
                        technician_serializer.validated_data['TECH_PASSWORD'] = make_password(request.data['TECH_PASSWORD'])
                        technician_serializer.validated_data['TECH_IMG'] = request.FILES.get('TECH_IMG', False)
                        technician_serializer.validated_data['TECH_ADDRESS'] = request.data['TECH_ADDRESS']

                        technician_serializer.save()

                        return JsonResponse({"message": "created successfully"}, status=200)
                    else:
                        return JsonResponse({"message":technician_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class LoginTechnician(APIView):

    def post(self, request):
        try:

            message = "no data found for given details"
            status = 404
            data = dict()
            mobile = request.POST.get('TECH_MOB').strip()
            password = request.POST.get('TECH_PASSWORD').strip().lower()

            technician = Technician.objects.get(TECH_MOB__iexact=mobile)

            if technician:
                if technician.TECH_STATUS=='Active':
                    check_pwd = check_password(password, technician.TECH_PASSWORD)
                    if check_pwd:
                        request.session['TECH_ID'] = technician.id
                        request.session['TECH_NAME'] = technician.TECH_NAME
                        request.session['TECH_EMAIL'] = technician.TECH_EMAIL
                        request.session['TECH_ADDRESS'] = technician.TECH_ADDRESS
                        request.session.create()
                        TechnicianLogin.objects.create(TECHNICIAN=technician, SESSION_ID=request.session.session_key,
                                                       LOGIN_DATETIME=datetime.datetime.now())

                        request.session['SESSION_ID'] = request.session.session_key
                        message = "technician logged in successfully"
                        status = 200
                        data['id'] = technician.id

                        data['redirect_url'] = "/dashboard"

                        return JsonResponse({"message": message, "data": data}, status=status)
                    else:
                        return JsonResponse({'error': str("Incorrect mobile number or password")}, status=500)
                else:
                    return JsonResponse({'error': str("Technician is not approved ")}, status=500)

        except Technician.DoesNotExist:
            return JsonResponse({'error': str("Technician does not exist")}, status=500)

        except Exception as error:
            print(error)
            info_message = "Something went wrong, please contact admin."
            logger.debug(info_message)
            logger.error(error, exc_info=True)
            return JsonResponse({'error': str(info_message)}, status=500)


class TechnicianLogout(APIView):
    def post(self, request):
        """
        Logout technician
        """
        try:
            if TechnicianLogin.objects.filter(SESSION_ID=request.session['SESSION_ID']).exists():
                technician_login = TechnicianLogin.objects.get(SESSION_ID=request.session['SESSION_ID'])
                technician_login.LOGOUT_DATETIME = timezone.now()
                technician_login.save()
                request.session.flush()
                return JsonResponse({"message": "logout successful"}, status=200)

        except Exception as error:

            info_message = "Something went wrong, please contact admin."
            logger.debug(info_message)
            logger.error(error, exc_info=True)
            return JsonResponse({'error': str(info_message)}, status=500)


class BasePage(APIView):
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session:
            is_authenticated=request.session['is_authenticated']
            print('1')
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            print('2')

            return HttpResponseRedirect(reverse_lazy('login'))

class DashboardPage(TemplateView):
    template_name='index.html'
    
class LoginPage(TemplateView):
    template_name='auth_login.html'