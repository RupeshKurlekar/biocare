from django.urls import path
from .views import RadiologistView, RadiologistReportMapView, RadiologistReportFilesView, RadiologistPmtView, RadiologistRegisterPage,RadiologistLoginPage, RadiologistBasePage, RadiologistListPage, RadiologistReportTechView, RadiologistReportsPage,RadiologistReportDetail,RadiologistReportDetailPage,PayRadiologistPage,PayRadiologistListView,PayRadiologistAPI,RadiologistPanelReportsPage,RadiologistPanelReportsReviewPage,RadiologistPanelReportsViewPage,RadiologistPatientsView,RadiologistPatientsHistoryView,RadiologistDetailsView,RadiologistUpdatePage,RadiologistUpdateView,RadiologistProfilePage,RadiologistChangePasswordPage,RadiologistChangePasswordAPIView

urlpatterns = [
    path('radiologists-api', RadiologistView.as_view(), name="radiologists-api"),
    path('rdlgreporttechnician/<id>', RadiologistReportTechView.as_view(), name="rdlgreporttechnician"),
    path('pay-radiologist-list-api/<id>', PayRadiologistListView.as_view(), name="pay-radiologist-list-api"),
    path('rdlgreport/<id>', RadiologistReportsPage.as_view(), name="rdlgreport"),
    path('rdlgreport-api/<id>', RadiologistReportMapView.as_view(), name="rdlgreport_api"),
    path('report-map-detail-api/<id>', RadiologistReportDetail.as_view(), name="report-map-detail-api"),
    path('view_radiologist_report/<id>', RadiologistReportDetailPage.as_view(), name="view_radiologist_report"),
    path('radiologist_patients/<id>', RadiologistPatientsView.as_view(), name="radiologist_patients"),
    path('radiologist_patients_history/<id>', RadiologistPatientsHistoryView.as_view(), name="radiologist_patients_history"),
    path('rdlgfile', RadiologistReportFilesView.as_view(), name="rdlgfile"),
    path('rdlgpmt', RadiologistPmtView.as_view(), name="rdlgpmt"),
    path('radiologist/register', RadiologistRegisterPage.as_view(), name="radiologist_register"),
    path('radiologist/login', RadiologistLoginPage.as_view(), name="radiologist_login"),
    path('radiologist/index', RadiologistBasePage.as_view(), name="radiologist_index"),
    path('radiologist/reports', RadiologistPanelReportsPage.as_view(), name="radiologist_reports"),
    path('radiologist/review_report/<id>', RadiologistPanelReportsReviewPage.as_view(), name="radiologist_review_reports"),
    path('radiologist/view_report/<id>', RadiologistPanelReportsViewPage.as_view(), name="radiologist_view_reports"),
    path('technician/radiologists', RadiologistListPage.as_view(), name="technician_radiologists"),
    path('technician/pay_radiologists', PayRadiologistPage.as_view(), name="technician_pay_radiologists"),
    path('add-transaction-api', PayRadiologistAPI.as_view(), name="add-transaction-api"),
    path('radiologist_details/<id>', RadiologistDetailsView.as_view(), name="radiologist_details"),
    path('radiologist/update_profile', RadiologistUpdatePage.as_view(), name="radiologist_update"),
    path('radiologist_update/<id>', RadiologistUpdateView.as_view(), name="radiologist_update"),
    path('radiologist/view_profile', RadiologistProfilePage.as_view(), name="radiologist_view_profile"),
    path('radiologist/change_password', RadiologistChangePasswordPage.as_view(), name="radiologist_change_password"),
    path('radiologist-change-password-api/<id>', RadiologistChangePasswordAPIView.as_view(), name="radiologist-change-password-api"),





]
