from django.urls import path
from .views import RadiologistView, RadiologistReportMapView, RadiologistReportFilesView, RadiologistPmtView, RadiologistRegisterPage,RadiologistLoginPage, RadiologistBasePage

urlpatterns = [
    path('radiologists-api', RadiologistView.as_view(), name="radiologists-api"),
    path('rdlgreport', RadiologistReportMapView.as_view(), name="rdlgreport"),
    path('rdlgfile', RadiologistReportFilesView.as_view(), name="rdlgfile"),
    path('rdlgpmt', RadiologistPmtView.as_view(), name="rdlgpmt"),
    path('radiologist/register', RadiologistRegisterPage.as_view(), name="radiologist_register"),
    path('radiologist/login', RadiologistLoginPage.as_view(), name="radiologist_login"),
    path('radiologist/index', RadiologistBasePage.as_view(), name="radiologist_index"),

]
