from django.urls import path
from .views import TechnicianView, LoginTechnician, TechnicianLogout, BasePage, DashboardPage, LoginPage


urlpatterns = [
    path('', BasePage.as_view(), name="base"),
    path('technician/index', DashboardPage.as_view(), name="home"),
    path('technician/login', LoginPage.as_view(), name="login"),
    path('technicians', TechnicianView.as_view(), name="technicians"),
    path('technician/login-api', LoginTechnician.as_view(), name="login-api"),
    path('technician/logout-api', TechnicianLogout.as_view(), name="logout-api"),

]
