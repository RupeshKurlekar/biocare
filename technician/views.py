import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from datetime import date,timedelta
from .models import TechnicianLogin, Technician,Wallet
from .serializers import TechnicianSerializers, TechnicianListSerializers, WalletSerializers
import logging
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from radiologist.models import Radiologist, RadiologistLogin, RadiologistReportMap
from reports.models import Report, Tickets
from master.models import Priority
from reports.serializers import ReportsListSerializer
from django.utils.decorators import method_decorator
from .decorator import isuserisLoggedIn
logger = logging.getLogger()


# Create your views here.
class TechnicianView(APIView):

    def get(self, request):
        """
        Get all Technician
        """
        try:
            serializer = TechnicianListSerializers(Technician.objects.filter(IS_APPROVED=True), many=True)
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


class LoginView(APIView):
    
    def post(self, request):
        try:

            message = "no data found for given details"
            status = 404
            data = dict()
            mobile = request.POST.get('MOB_NO')
            password = request.POST.get('PASSWORD')
            login_type = request.POST.get('TYPE')
            if login_type=="technician":
                technician = Technician.objects.get(TECH_MOB__iexact=mobile)
                if technician:
                    if technician.IS_APPROVED:

                        print('password',password,technician.TECH_PASSWORD)
                        check_pwd = check_password(password, technician.TECH_PASSWORD)
                        print('checkpwd',check_pwd)
                        if check_pwd:
                            request.session.flush()
                            request.session['TECH_ID'] = technician.id
                            request.session['TECH_NAME'] = technician.TECH_NAME
                            request.session['TECH_EMAIL'] = technician.TECH_EMAIL
                            request.session['TECH_ADDRESS'] = technician.TECH_ADDRESS
                            request.session['is_authenticated'] = True
                            request.session['type']="technician"
                            request.session.create()
                            TechnicianLogin.objects.create(TECHNICIAN=technician, SESSION_ID=request.session.session_key,
                                                        LOGIN_DATETIME=datetime.datetime.now())

                            request.session['SESSION_ID'] = request.session.session_key
                            message = "technician logged in successfully"
                            status = 200
                            data['id'] = technician.id


                            data['redirect_url'] = "/technician/index"

                            return JsonResponse({"message": message, "data": data}, status=status)
                        else:
                            return JsonResponse({'error': str("Incorrect mobile number or password")}, status=500)
                    else:
                        return JsonResponse({'error': str("Technician is not approved ")}, status=500)
            
            if login_type=="radiologist":
                radiologist = Radiologist.objects.get(RDLG_MOB_NO__iexact=mobile)
                if radiologist:
                    if radiologist.IS_APPROVED:
                        check_pwd = check_password(password, radiologist.RDLG_PASSWORD)
                        if check_pwd:
                            request.session.flush()
                            request.session['RDLG_ID'] = radiologist.id
                            request.session['RDLG_NAME'] = radiologist.RDLG_NAME
                            request.session['RDLG_EMAIL'] = radiologist.RDLG_EMAIL
                            request.session['is_authenticated'] = True
                            request.session['type']="radiologist"
                            request.session.create()
                            RadiologistLogin.objects.create(RADIOLOGIST=radiologist, SESSION_ID=request.session.session_key,
                                                        LOGIN_DATETIME=datetime.datetime.now())

                            request.session['SESSION_ID'] = request.session.session_key
                            message = "radiologist logged in successfully"
                            status = 200
                            data['id'] = radiologist.id


                            data['redirect_url'] = "/radiologist/index"

                            return JsonResponse({"message": message, "data": data}, status=status)
                        else:
                            return JsonResponse({'error': str("Incorrect mobile number or password")}, status=500)
                    else:
                        return JsonResponse({'error': str("Radiologist is not approved ")}, status=500)

        except Technician.DoesNotExist:
            return JsonResponse({'error': str("Technician does not exist")}, status=500)
        except Radiologist.DoesNotExist:
            return JsonResponse({'error': str("Radiologist does not exist")}, status=500)

        except Exception as error:
            print(error)
            info_message = "Something went wrong, please contact admin."
            logger.debug(info_message)
            logger.error(error, exc_info=True)
            return JsonResponse({'error': str(info_message)}, status=500)


class LogoutView(APIView):
    def post(self, request):
        """
        Logout technician
        """
        try:
            login_type = request.POST.get('TYPE')
            if login_type=="technician":
                if TechnicianLogin.objects.filter(SESSION_ID=request.session['SESSION_ID']).exists():
                    technician_login = TechnicianLogin.objects.get(SESSION_ID=request.session['SESSION_ID'])
                    technician_login.LOGOUT_DATETIME = timezone.now()
                    technician_login.save()
                    request.session.flush()
                    return JsonResponse({"message": "logout successful"}, status=200)
            elif login_type=="radiologist":
                if RadiologistLogin.objects.filter(SESSION_ID=request.session['SESSION_ID']).exists():
                    radiologist_login = RadiologistLogin.objects.get(SESSION_ID=request.session['SESSION_ID'])
                    radiologist_login.LOGOUT_DATETIME = timezone.now()
                    radiologist_login.save()
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
        if "is_authenticated" in request.session and request.session['type'] == "technician":
            is_authenticated=request.session['is_authenticated']
            print('1')
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return HttpResponseRedirect(reverse_lazy('login'))



class DashboardPage(APIView):

    @isuserisLoggedIn()
    def get(self,request):
        if request.session['type'] == "technician":
            return render(request, 'index.html',{})
        else:
            return HttpResponseRedirect(reverse_lazy('login'))


class LoginPage(APIView):
    def get(self,request):

        return render(request, 'auth_login.html',{"type":"Technician"})

class TechnicianRegisterPage(APIView):
    def get(self,request):
        return render(request, 'register.html')

class TechnicianTransactionLogPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session:
            
            is_authenticated=request.session['is_authenticated']
            return render(request, 'transaction_log.html',{"is_authenticated":is_authenticated})

class TechnicianSendPatientHistoryPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        is_authenticated=False
        if "is_authenticated" in request.session:
            is_authenticated=request.session['is_authenticated']
            return render(request, 'send_patient_history.html',{"is_authenticated":is_authenticated})

class TechnicianUpdateProfilePage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session:
            is_authenticated=request.session['is_authenticated']
            return render(request, 'update_profile.html',{"is_authenticated":is_authenticated})

class TechnicianProfilePage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        is_authenticated=False
        if "is_authenticated" in request.session:

            is_authenticated=request.session['is_authenticated']
            return render(request, 'view_profile.html',{"is_authenticated":is_authenticated})

class TechnicianChangePasswordPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        return render(request, 'change_password.html')
    










class TechnicianDetailsView(APIView):

    def get(self, request, id):
        """
        Get technician details
        """
        try:
            serializer = TechnicianListSerializers(Technician.objects.get(pk=id))
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class WalletView(APIView):

    def get(self, request, id):
        """
        Get technician wallet amount
        """
        try:
            if Wallet.objects.filter(TECHNICIAN=id).exists():
                serializer = WalletSerializers(Wallet.objects.get(TECHNICIAN=id))
                return JsonResponse({"IsAmountPresent": True, "data": serializer.data}, status=200)
            else:
                return JsonResponse({"IsAmountPresent": False, "data": ""}, status=200)

        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class ChangePasswordAPIView(APIView):

    def post(self, request, id):
        """
        change technician password
        """
        try:
            if request.data['TECH_OLD_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter old password"}, status=500)
            if request.data['TECH_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter new  password"}, status=500)
            else:
                password=request.data['TECH_OLD_PASSWORD']
                technician=Technician.objects.get(id=id)
                if technician:
                    print('password',password,request.data['TECH_PASSWORD'])
                    check_pwd = check_password(password, technician.TECH_PASSWORD)
                    if check_pwd:
                        new_password=make_password(request.data['TECH_PASSWORD'])
                        technician.TECH_PASSWORD=new_password
                        technician.save()
            
                        return JsonResponse({"message":"Password changes successfully"}, status=200)
                    else:
                        return JsonResponse({"message": "Old password did not match"}, status=500)
                else:
                    return JsonResponse({"data": ""}, status=200)

        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)


class TechnicianUpdateView(APIView):
    def post(self, request,id):
        """
        Update Technician data
        """
        try:

            if request.data['TECH_NAME'] == "":
                return JsonResponse({'error': "PLease enter name"}, status=500)
            if request.data['TECH_MOB'] == "":
                return JsonResponse({'error': "PLease enter Mobile Number"}, status=500)
            if request.data['TECH_EMAIL'] == "":
                return JsonResponse({'error': "PLease enter Email"}, status=500)
            
            if request.data['TECH_ADDRESS'] == "":
                return JsonResponse({'error': "PLease enter ADDRESS"}, status=500)
            else:
                if Technician.objects.filter(TECH_MOB=request.data['TECH_MOB']).exclude(id=id).exists():
                    return JsonResponse({'error': "Mobile Number already exists"}, status=500)
                else:

                    

                    technician=Technician.objects.get(id=id)
                    technician.TECH_NAME = request.data['TECH_NAME']
                    technician.TECH_MOB = request.data['TECH_MOB']
                    technician.TECH_EMAIL = request.data['TECH_EMAIL']
                    
                    technician.TECH_ADDRESS = request.data['TECH_ADDRESS']
                    if request.FILES.get('TECH_IMG'):
                        profile_picture=request.FILES.get('TECH_IMG')
                        technician.TECH_IMG = profile_picture
                    technician.save()

                    return JsonResponse({"message": "updated successfully"}, status=200)
               

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)

class HomePageStats(APIView):
    def get(self,request,type):
        """
        Get homepage stats
        """
        try:
            if type=='technician':
                priorities=Priority.objects.all()
                priority_obj=[]
                week_start = date.today()
                week_start -= timedelta(days=week_start.weekday())
                week_end = week_start + timedelta(days=7)
                for i in range(len(priorities)):
                    total_reports=Report.objects.filter(IS_DELETED=False).filter(PATIENT__TECHNICIAN=request.session['TECH_ID']).filter(RP_PRIORITY=priorities[i].id)
                    assigned_reports=[]
                    pending_reports=[]
                    completed_reports=[]
                    todays_report=[]
                    requested_tickets_report=[]
                    weekly_report=[]
                    for j in range(len(total_reports)):
                        queryset=RadiologistReportMap.objects.filter(REPORT=total_reports[j].id)
                        assigned_reports.append(queryset.count())
                        pending_reports.append(queryset.filter(RP_STATUS__STATUS__iexact="pending").count())
                        completed_reports.append(queryset.filter(RP_STATUS__STATUS__iexact="completed").count())
                        todays_report.append(total_reports.filter(CREATED_DATE=datetime.date.today()).count())
                        weekly_report.append(total_reports.filter(CREATED_DATE__gte=week_start,CREATED_DATE__lt=week_end).count())
                        requested_tickets_report.append(Tickets.objects.filter(REPORT=total_reports[j].id).count())
                    priority_obj.append({priorities[i].PRIORITY:{"total_reports":total_reports.count(),"assigned_reports":sum(assigned_reports),"pending_reports":sum(pending_reports),"completed_reports":sum(completed_reports),"todays_report":sum(todays_report),"requested_ticket_report":sum(requested_tickets_report),"weekly_report":list(set(weekly_report))}})
                return JsonResponse({"message": "listed all", "data": priority_obj}, status=200)
            # if type=='radiologist':

        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

