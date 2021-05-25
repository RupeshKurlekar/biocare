from django.urls import path
from .views import LoginSuper, SuperLogout, BasePage, DashboardPage, LoginPage


urlpatterns = [
    path('', BasePage.as_view(), name="base"),
    path('super/index', DashboardPage.as_view(), name="home"),
    path('super/login', LoginPage.as_view(), name="login"),
    path('super/login-api', LoginSuper.as_view(), name="login-api"),
    path('super/logout-api', SuperLogout.as_view(), name="logout-api"),

]
