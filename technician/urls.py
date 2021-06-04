from django.urls import path
from .views import TechnicianView, LogoutView, BasePage, DashboardPage, LoginPage,TechnicianRegisterPage,LoginView,TechnicianTransactionLogPage,TechnicianSendPatientHistoryPage,TechnicianUpdateProfilePage,TechnicianDetailsView,TechnicianUpdateView, WalletView,TechnicianProfilePage,TechnicianChangePasswordPage,ChangePasswordAPIView,HomePageStats


urlpatterns = [
    path('', BasePage.as_view(), name="base"),
    path('technician/index', DashboardPage.as_view(), name="home"),
    path('technician/login', LoginPage.as_view(), name="login"),
    path('technician/register', TechnicianRegisterPage.as_view(), name="technician_register"),
    path('technician/transaction_log', TechnicianTransactionLogPage.as_view(), name="technician_transaction_log"),
    path('technician/send_patient_history', TechnicianSendPatientHistoryPage.as_view(), name="technician_send_patient_history"),
    path('technician/update_profile', TechnicianUpdateProfilePage.as_view(), name="technician_update_profile"),
    path('technician/view_profile', TechnicianProfilePage.as_view(), name="view_profile"),
    path('technician/change_password', TechnicianChangePasswordPage.as_view(), name="change_password"),
    path('technician_details/<id>', TechnicianDetailsView.as_view(), name="technician_details"),
    path('technician_update/<id>', TechnicianUpdateView.as_view(), name="technician_update"),
    path('change-password-api/<id>', ChangePasswordAPIView.as_view(), name="change_password"),
    path('technicians', TechnicianView.as_view(), name="technicians"),
    path('login-api', LoginView.as_view(), name="login-api"),
    path('wallet-api/<id>', WalletView.as_view(), name="wallet-api"),
    path('homepage-stats-api/<type>', HomePageStats.as_view(), name="homepage-stats-api"),
    path('logout-api', LogoutView.as_view(), name="logout-api"),

]
