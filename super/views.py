import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView

from .models import SuperLogin, Super
from .serializers import SuperSerializers, SuperListSerializers
import logging
from django.urls import reverse_lazy
from django.views.generic import TemplateView
logger = logging.getLogger()


# Create your views here.


class LoginSuper(APIView):

    def post(self, request):
        try:

            message = "no data found for given details"
            status = 404
            data = dict()
            mobile = request.POST.get('SUPER_MOB').strip()
            password = request.POST.get('SUPER_PASSWORD').strip().lower()

            super = Super.objects.get(SUPER_MOB__iexact=mobile)

            if super:
                if super.SUPER_STATUS=='Active':
                    check_pwd = check_password(password, super.TECH_PASSWORD)
                    if check_pwd:
                        request.session['SUPER_ID'] = super.id
                        request.session['SUPER_NAME'] = super.SUPER_NAME
                        request.session['SUPER_EMAIL'] = super.SUPER_EMAIL
                        request.session.create()
                        TechnicianLogin.objects.create(SUPER=super, SESSION_ID=request.session.session_key,
                                                       LOGIN_DATETIME=datetime.datetime.now())

                        request.session['SESSION_ID'] = request.session.session_key
                        message = "super user logged in successfully"
                        status = 200
                        data['id'] = super.id

                        data['redirect_url'] = "/dashboard"

                        return JsonResponse({"message": message, "data": data}, status=status)
                    else:
                        return JsonResponse({'error': str("Incorrect mobile number or password")}, status=500)
                else:
                    return JsonResponse({'error': str("Super is not approved ")}, status=500)

        except Super.DoesNotExist:
            return JsonResponse({'error': str("Super does not exist")}, status=500)

        except Exception as error:
            print(error)
            info_message = "Something went wrong, please contact admin."
            logger.debug(info_message)
            logger.error(error, exc_info=True)
            return JsonResponse({'error': str(info_message)}, status=500)


class SuperLogout(APIView):
    def post(self, request):
        """
        Logout super
        """
        try:
            if SuperLogin.objects.filter(SESSION_ID=request.session['SESSION_ID']).exists():
                super_login = SuperLogin.objects.get(SESSION_ID=request.session['SESSION_ID'])
                super_login.LOGOUT_DATETIME = timezone.now()
                super_login.save()
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

class SuperChangePasswordPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        return render(request, 'super_change_password.html')

class ChangePasswordAPIView(APIView):

    def post(self, request, id):
        """
        change super password
        """
        try:
            if request.data['SUPER_OLD_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter old password"}, status=500)
            if request.data['SUPER_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter new  password"}, status=500)
            else:
                password=request.data['SUPER_OLD_PASSWORD']
                super=Super.objects.get(id=id)
                if super:
                    print('password',password,request.data['SUPER_PASSWORD'])
                    check_pwd = check_password(password, super.SUPER_PASSWORD)
                    if check_pwd:
                        new_password=make_password(request.data['SUPER_PASSWORD'])
                        super.SUPER_PASSWORD=new_password
                        super.save()
            
                        return JsonResponse({"message":"Password changes successfully"}, status=200)
                    else:
                        return JsonResponse({"message": "Old password did not match"}, status=500)
                else:
                    return JsonResponse({"data": ""}, status=200)

        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class SuperDetailsView(APIView):

    def get(self, request, id):
        """
        Get super details
        """
        try:
            serializer = SuperListSerializers(Super.objects.get(pk=id))
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class SuperProfilePage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        is_authenticated=False
        if "is_authenticated" in request.session:

            is_authenticated=request.session['is_authenticated']
            return render(request, 'super_view_profile.html',{"is_authenticated":is_authenticated})

class DashboardPage(TemplateView):
    template_name='super_index.html'
    
class LoginPage(TemplateView):
    template_name='auth_login.html'

class TechnicianApprovalPage(TemplateView):
    template_name= 'super_technician-approval.html'

class RadiologistApprovalPage(TemplateView):
    template_name= 'super_radiologists-approval.html'

class TechnicianPage(TemplateView):
    template_name= 'super_technician.html'

class RadiologistPage(TemplateView):
    template_name= 'super_radiologists.html'

class PatientsPage(TemplateView):
    template_name= 'super_patients.html'

class AllReportPage(TemplateView):
    template_name= 'super_reports.html'

class TicketListPage(TemplateView):
    template_name= 'super_tickets.html'

class PriorityMastersPage(TemplateView):
    template_name= 'super_priority-masters.html'

class ServicesMasterPage(TemplateView):
    template_name= 'super_services-master.html'

class PaymentManagementPage(TemplateView):
    template_name= 'super_pay_radiologists.html'