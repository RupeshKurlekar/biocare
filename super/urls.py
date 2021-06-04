from django.urls import path
from .views import LoginSuper, SuperLogout, BasePage, DashboardPage, LoginPage, TechnicianApprovalPage, RadiologistApprovalPage,TechnicianPage,RadiologistPage, PatientsPage , AllReportPage, TicketListPage, PriorityMastersPage, ServicesMasterPage, PaymentManagementPage


urlpatterns = [
    path('', BasePage.as_view(), name="base"),
    path('super/index', DashboardPage.as_view(), name="home"),
    path('super/login', LoginPage.as_view(), name="login"),
    path('super/login-api', LoginSuper.as_view(), name="login-api"),
    path('super/logout-api', SuperLogout.as_view(), name="logout-api"),
    path('super/change_password', SuperChangePasswordPage.as_view(), name="change_password"),
    path('change-password-api/<id>', ChangePasswordAPIView.as_view(), name="change_password"),
    path('super/technician-approval',TechnicianApprovalPage.as_view(),name="technician_approval"),
    path('super/radiologist-approval',RadiologistApprovalPage.as_view(),name="radiologist_approval"),
    path('super/technician',TechnicianPage.as_view(),name="technician"),
    path('super/radiologist',RadiologistPage.as_view(),name="radiologists"),
    path('super/patients',PatientsPage.as_view(),name="patients"),
    path('super/all_reports',AllReportPage.as_view(),name="all_reports"),
    path('super/ticket-list',TicketListPage.as_view(),name="ticket_list"),
    path('super/priority-masters',PriorityMastersPage.as_view(),name="priority_masters"),
    path('super/services-master',ServicesMasterPage.as_view(),name="services_master"),
    path('super/payment-management',PaymentManagementPage.as_view(),name="payment_management")
    path('super/view_profile', SuperProfilePage.as_view(), name="view_profile"),
    path('super-detail-view-api/<id>', SuperDetailsView.as_view(), name="superdetails_view"),


]
 