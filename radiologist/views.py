from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from technician.models import Technician, Wallet
from master.models import Priority, ReportStatus
from reports.models import Report
from .models import RadiologistPmt, RadiologistReportFiles, RadiologistReportMap, Radiologist,RadiologistPriority,TransactionLog
from .serializers import RadiologistSerializers, RadiologistReportMapSerializers, RadiologistReportFilesSerializers,RadiologistPmtSerializers,RadiologistReportSerializers,RadiologistReportDetailSerializers,TransactionLogSerializer,TransactionLogListSerializer
import logging
from django.views.generic import TemplateView
from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
logger = logging.getLogger()
from technician.decorator import isuserisLoggedIn
from django.urls import reverse_lazy
from patient.serializers import PatientHistorySerializers, PatientSerializers
from patient.models import Patient, PatientHistory

# Create your views here.
class RadiologistView(APIView):

    def get(self, request):
        """
        Get all Radiologist
        """
        try:
            serializer = RadiologistSerializers(Radiologist.objects.filter(IS_APPROVED=True).filter(RDLG_TYPE="1"), many=True)
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
            if request.data['RDLG_MOB_NO'] == "":
                return JsonResponse({'error': "PLease enter mobile number "}, status=500)
            if request.data['RDLG_EMAIL'] == "":
                return JsonResponse({'error': "PLease enter email "}, status=500)
            if request.data['RDLG_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter password "}, status=500)
            if request.data['RDLG_ADDRESS'] == "":
                return JsonResponse({'error': "PLease enter address "}, status=500)
            if request.data['RDLG_AREA'] == "":
                return JsonResponse({'error': "PLease enter area "}, status=500)
            if request.data['RDLG_QUALIFICATION'] == "":
                return JsonResponse({'error': "PLease enter qualification "}, status=500)
            if request.data['RDLG_EXPERIENCE'] == "":
                return JsonResponse({'error': "PLease enter experience "}, status=500)
            if request.data['RDLG_SPECIALITY'] == "":
                return JsonResponse({'error': "PLease enter speciality "}, status=500)
            if request.data['RDLG_TYPE'] == "":
                return JsonResponse({'error': "PLease enter type "}, status=500)
            if request.data['RDLG_GST'] == "":
                return JsonResponse({'error': "PLease enter if GST or not"}, status=500)
            if not request.FILES.get('RDLG_IMG',False):
                return JsonResponse({'error': "PLease upload image"}, status=500)
            
            else:
                if Radiologist.objects.filter(RDLG_MOB_NO=request.data['RDLG_MOB_NO']).exists():
                    return JsonResponse({'error': "Mobile Number already exists"}, status=500)
                else:
                    print(type(request.data['TECHNICIAN']),request.data['TECHNICIAN'])
                    if request.data['TECHNICIAN']=="":
                        TECHNICIAN=""
                    else:
                        TECHNICIAN=Technician.objects.get(
                            id=request.data['TECHNICIAN'])

                    radiologist_serializer = RadiologistSerializers(data=request.data)

                    if radiologist_serializer.is_valid():
                        if Radiologist.objects.exists():
                            ID = Radiologist.objects.last()
                            RDLG_ID = 'RDLG_' + str(ID.id + 1)
                        else:
                            RDLG_ID = 'RDLG_1'
                        radiologist_serializer.validated_data['RDLG_ID'] = RDLG_ID
                        if TECHNICIAN:

                            radiologist_serializer.validated_data['TECHNICIAN'] = TECHNICIAN
                        
                        radiologist_serializer.validated_data['RDLG_PASSWORD'] = make_password(request.data['RDLG_PASSWORD'])

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


class RadiologistReportTechView(APIView):

    def get(self, request,id):
        """
        Get all sellers
        """
        try:
            if Radiologist.objects.filter(Q(TECHNICIAN=id)| Q(RDLG_TYPE="2")).exists():
                radiologist_queryset=Radiologist.objects.filter(Q(TECHNICIAN=id)|Q(RDLG_TYPE="2"))
                report_list=[]

                for i in range(len(radiologist_queryset)):
                    reports=RadiologistReportMap.objects.filter(RADIOLOGIST=radiologist_queryset[i].id).first()
                    report_list.append(reports)
                serializer = RadiologistReportMapSerializers(report_list, many=True)
                return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
            else:
                return JsonResponse({"message": "listed all", "data":""}, status=200)

           
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


class RadiologistRegisterPage(TemplateView):
    template_name='radiologist_register.html'

class RadiologistPanelReportsPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if request.session['type']=="radiologist":
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'radiologist_radiologist_reports.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))

class RadiologistPanelReportsReviewPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,id):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if request.session['type']=="radiologist":
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'radiologist_review_report.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))

class RadiologistPanelReportsViewPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,id):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if request.session['type']=="radiologist":
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'radiologist_view_report.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))




class RadiologistLoginPage(APIView):
    def get(self,request):
        return render(request, 'auth_login.html',{"type":"Radiologist"})

class RadiologistBasePage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        if "type" in request.session:
            if request.session['type']=="radiologist":
                return render(request, 'radiologist_index.html')
            else:
                return HttpResponseRedirect(reverse_lazy('login'))        
        return HttpResponseRedirect(reverse_lazy('login'))



class RadiologistListPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        if "type" in request.session:
            if request.session['type']=="technician":
                return render(request, 'radiologists.html')
            else:
                return HttpResponseRedirect(reverse_lazy('login'))        
        return HttpResponseRedirect(reverse_lazy('login'))

class RadiologistReportsPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,id):
        if "type" in request.session:
            if request.session['type']=="technician":
                return render(request, 'technician_radiologist_reports.html')
            else:
                return HttpResponseRedirect(reverse_lazy('login'))        
        return HttpResponseRedirect(reverse_lazy('login'))

class RadiologistReportDetailPage(APIView):
    @isuserisLoggedIn()
    def get(self,request,id):
        if "type" in request.session:
            if request.session['type']=="technician":
                return render(request, 'view_radiologist_report.html')
            else:
                return HttpResponseRedirect(reverse_lazy('login'))        
        return HttpResponseRedirect(reverse_lazy('login'))




class PayRadiologistPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):
        
        if "type" in request.session:
            if request.session['type']=="technician":
                return render(request, 'pay_radiologists.html')
            else:
                return HttpResponseRedirect(reverse_lazy('login'))
        return HttpResponseRedirect(reverse_lazy('login'))
        

class RadiologistReportMapView(APIView):

    def get(self, request,id):
       
        try:
            serializer = RadiologistReportSerializers(RadiologistReportMap.objects.filter(RADIOLOGIST=id), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class RadiologistReportDetail(APIView):

    def get(self, request,id):
       
        try:
            serializer = RadiologistReportDetailSerializers(RadiologistReportMap.objects.get(REPORT=id))
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class PayRadiologistListView(APIView):

    def get(self, request,id):
        """
        Get all sellers
        """
        try:
            if Radiologist.objects.filter(Q(TECHNICIAN=id)| Q(RDLG_TYPE="2")).exists():
                radiologist_queryset=Radiologist.objects.filter(Q(TECHNICIAN=id)|Q(RDLG_TYPE="2"))
                report_list=[]
                radiologist_amount_obj=[]
                for i in range(len(radiologist_queryset)):
                    amount=[]
                    due_amount=[]
                    no_of_reports=[]
                    
                    reports=RadiologistReportMap.objects.filter(RADIOLOGIST=radiologist_queryset[i].id)
                    for j in range(len(reports)):
                        no_of_reports.append(j)
                        if RadiologistPriority.objects.filter(RADIOLOGIST=reports[j].RADIOLOGIST.id).filter(PRIORITY=reports[j].REPORT.RP_PRIORITY.id).exists():
                            amount_queryset=RadiologistPriority.objects.filter(RADIOLOGIST=reports[j].RADIOLOGIST.id).filter(PRIORITY=reports[j].REPORT.RP_PRIORITY.id)
                            
                            for k in range(len(amount_queryset)):
                                amount.append(amount_queryset[k].RADIOLOGIST_PRICE)

                        else:
                            priority_queryset=Priority.objects.filter(id=reports[j].REPORT.RP_PRIORITY.id)
                            for l in range(len(priority_queryset)):
                                amount.append(int(priority_queryset[l].RATE))

                        

                    for m in range(len(reports)):
                        if TransactionLog.objects.filter(RADIOLOGIST=reports[m].RADIOLOGIST.id).exists():
                            due_queryset=TransactionLog.objects.filter(RADIOLOGIST=reports[m].RADIOLOGIST.id)
                            for n in range(len(due_queryset)):
                                due_amount.append(int(due_queryset[n].AMOUNT))
                            total_due_amount=sum(amount)-sum(due_amount)
                        else:
                            total_due_amount=sum(amount)
                    serializer=RadiologistReportMapSerializers(reports[j]).data
                    modified_data={"total_amount":sum(amount),"total_due_amount":total_due_amount,"total_reports":len(no_of_reports)}
                    modified_data.update(serializer)
                    report_list.append(modified_data)
                
                return JsonResponse({"message": "listed all", "data": report_list}, status=200)
            else:
                return JsonResponse({"message": "listed all", "data":"","total_amount":"","total_due_amount":"","total_reports":""}, status=200)

           
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)


class PayRadiologistAPI(APIView):
    def get(self, request):
       
        try:
            serializer = TransactionLogListSerializer(TransactionLog.objects.all(), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)
    
    def post(self, request):
        try:
            if request.data['AMOUNT'] == "":
                return JsonResponse({'error': "PLease enter amount "}, status=500)
            if request.data['REPORTS_COUNT'] == "":
                return JsonResponse({'error': "PLease enter reports count"}, status=500)
            if request.data['REPORTS_DESCRIPTION'] == "":
                return JsonResponse({'error': "PLease enter reports description"}, status=500)

            else:
                transaction_serializer = TransactionLogSerializer(data=request.data)

                if transaction_serializer.is_valid():
                    if TransactionLog.objects.exists():
                        ID = TransactionLog.objects.last()
                        TRANS_ID = 'TRANS_' + str(ID.id + 1)
                    else:
                        TRANS_ID = 'TRANS_1'
                    transaction_serializer.validated_data['TRANS_ID'] = TRANS_ID
                    transaction_serializer.validated_data['TECHNICIAN'] = Technician.objects.get(id=request.data['TECHNICIAN'])
                    transaction_serializer.validated_data['RADIOLOGIST'] = Radiologist.objects.get(
                        id=request.data['RADIOLOGIST'])


                    transaction_serializer.save()
                    wallet_obj=Wallet.objects.filter(TECHNICIAN=request.data['TECHNICIAN']).last()
                    wallet_amt=int(wallet_obj.WALLET_AMT)
                    new_wallet_amt=wallet_amt-int(request.data['AMOUNT'])
                    wallet_obj.WALLET_AMT=new_wallet_amt
                    wallet_obj.save()

                    return JsonResponse({"message": "created successfully"}, status=200)
                else:
                    return JsonResponse({"message": transaction_serializer.errors}, status=500)

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)


class RadiologistPatientsView(APIView):

    def get(self, request,id):
       
        try:
            if RadiologistReportMap.objects.filter(RADIOLOGIST=id).exists():

                radiologist_map=RadiologistReportMap.objects.filter(RADIOLOGIST=id)
                patients_list=[]
                for i in range(len(radiologist_map)):
                    report=Report.objects.get(id=radiologist_map[i].REPORT.id)
                    patients_list.append(report.PATIENT.id)
            serializer = PatientSerializers(Patient.objects.filter(id__in=list(set(patients_list))), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class RadiologistPatientsHistoryView(APIView):

    def get(self, request,id):
       
        try:
            if RadiologistReportMap.objects.filter(RADIOLOGIST=id).exists():

                radiologist_map=RadiologistReportMap.objects.filter(RADIOLOGIST=id)
                patients_list=[]
                for i in range(len(radiologist_map)):
                    report=Report.objects.get(id=radiologist_map[i].REPORT.id)
                    patients_list.append(report.PATIENT.id)
            
            serializer = PatientHistorySerializers(PatientHistory.objects.filter(PATIENT__id__in=list(set(patients_list))), many=True)
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class RadiologistDetailsView(APIView):

    def get(self, request, id):
        """
        Get radiologist details
        """
        try:
            serializer = RadiologistSerializers(Radiologist.objects.get(pk=id))
            return JsonResponse({"message": "listed all", "data": serializer.data}, status=200)
        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)

class RadiologistUpdatePage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if request.session['type']=="radiologist":
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'radiologist_update_profile.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))

class RadiologistUpdateView(APIView):
    def post(self, request,id):
        """
        Update radiologist data
        """
        try:

            if request.data['RDLG_NAME'] == "":
                return JsonResponse({'error': "PLease enter name"}, status=500)
            if request.data['RDLG_MOB_NO'] == "":
                return JsonResponse({'error': "PLease enter mobile number"}, status=500)
            if request.data['RDLG_EMAIL'] == "":
                return JsonResponse({'error': "PLease enter email"}, status=500)
            if request.data['RDLG_ADDRESS'] == "":
                return JsonResponse({'error': "PLease enter address"}, status=500)
            if request.data['RDLG_AREA'] == "":
                return JsonResponse({'error': "PLease enter area"}, status=500)
            if request.data['RDLG_QUALIFICATION'] == "":
                return JsonResponse({'error': "PLease enter qualification"}, status=500)
            if request.data['RDLG_EXPERIENCE'] == "":
                return JsonResponse({'error': "PLease enter experience"}, status=500)
            if request.data['RDLG_SPECIALITY'] == "":
                return JsonResponse({'error': "PLease enter speciality"}, status=500)
            else:
                if Radiologist.objects.filter(RDLG_MOB_NO=request.data['RDLG_MOB_NO']).exclude(id=id).exists():
                    return JsonResponse({'error': "Mobile Number already exists"}, status=500)
                else:

                    

                    radiologist=Radiologist.objects.get(id=id)
                    radiologist.RDLG_NAME = request.data['RDLG_NAME']
                    radiologist.RDLG_MOB_NO = request.data['RDLG_MOB_NO']
                    radiologist.RDLG_EMAIL = request.data['RDLG_EMAIL']
                    radiologist.RDLG_AREA = request.data['RDLG_AREA']
                    radiologist.RDLG_QUALIFICATION = request.data['RDLG_QUALIFICATION']
                    radiologist.RDLG_EXPERIENCE = request.data['RDLG_EXPERIENCE']
                    radiologist.RDLG_SPECIALITY = request.data['RDLG_SPECIALITY']
                    radiologist.RDLG_ADDRESS = request.data['RDLG_ADDRESS']
                    if request.FILES.get('RDLG_IMG'):
                        profile_picture=request.FILES.get('RDLG_IMG')
                        radiologist.RDLG_IMG = profile_picture
                    radiologist.save()

                    return JsonResponse({"message": "updated successfully"}, status=200)
               

        except Exception as error:
            info_message = "Internal Server Error"
            logger.error(info_message, error)
            return JsonResponse({'error': str(info_message)}, status=500)

class RadiologistProfilePage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if request.session['type']=="radiologist":
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'radiologist_view_profile.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))

class RadiologistChangePasswordPage(APIView):
    @isuserisLoggedIn()
    def get(self,request):

        is_authenticated=False
        if "is_authenticated" in request.session and "type" in request.session:
            if request.session['type']=="radiologist":
                type=request.session['type']
                is_authenticated=request.session['is_authenticated']
                return render(request, 'radiologist_change_password.html',{"is_authenticated":is_authenticated,"type":type})
            else:
                return HttpResponseRedirect(reverse_lazy('login'))

class RadiologistChangePasswordAPIView(APIView):

    def post(self, request, id):
        """
        change radiologist password
        """
        try:
            if request.data['RDLG_OLD_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter old password"}, status=500)
            if request.data['RDLG_PASSWORD'] == "":
                return JsonResponse({'error': "PLease enter new  password"}, status=500)
            else:
                password=request.data['RDLG_OLD_PASSWORD']
                print('pass',password,request.data['RDLG_PASSWORD'])
                radiologist=Radiologist.objects.get(id=id)
                if radiologist:
                    check_pwd = check_password(password, radiologist.RDLG_PASSWORD)
                    print('check_pwd',check_pwd)
                    if check_pwd:
                        new_password=make_password(request.data['RDLG_PASSWORD'])
                        radiologist.RDLG_PASSWORD=new_password
                        radiologist.save()
            
                        return JsonResponse({"message":"Password changed successfully"}, status=200)
                    else:
                        return JsonResponse({"message": "Old password did not match"}, status=500)
                else:
                    return JsonResponse({"data": ""}, status=200)

        except Exception as e:
            info_message = "Internal Server Error"
            logger.error(info_message, e)
            return JsonResponse({'error': str(info_message)}, status=500)