from django.urls import path
from .views import TechnicianView, LogoutView, BasePage, DashboardPage, LoginPage,TechnicianRegisterPage,LoginView


urlpatterns = [
    path('', BasePage.as_view(), name="base"),
    path('technician/index', DashboardPage.as_view(), name="home"),
    path('technician/login', LoginPage.as_view(), name="login"),
    path('technician/register', TechnicianRegisterPage.as_view(), name="technician_register"),
    path('technicians', TechnicianView.as_view(), name="technicians"),
    path('login-api', LoginView.as_view(), name="login-api"),
    path('logout-api', LogoutView.as_view(), name="logout-api"),

]
