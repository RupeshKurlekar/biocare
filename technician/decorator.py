from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from technician.models import TechnicianLogin
# from radiologist.models import Radiologist
# from buyers.models import BuyerLogin

def isuserisLoggedIn():
    """
    Decorder checks permission for requested url and method with session.
    """
    def inner(func):
        def wrap(self, request, *args, **kwargs):
            if "SESSION_ID" in request.session:
                if request.session['type'] == "technician":
                    request.session['is_authenticated'] = True
                    return func(self, request, *args, **kwargs)
                if request.session['type'] == "radiologist":
                    
                    request.session['is_authenticated'] = True
                    return func(self, request, *args, **kwargs)
                # if request.session['TYPE'] == "EXHIBITOR":
                #     request.session['is_authenticated'] = True
                #     return func(self, request, *args, **kwargs)
                # if request.session['TYPE'] == "BUYER":
                #     request.session['is_authenticated'] = True
                #     return func(self, request, *args, **kwargs)
            else:
                
                # request.session['REDIRECT_URL'] = request.path_info
                # if "/spotexhibition/" in request.session['REDIRECT_URL']:
                #     request.session['REDIRECT_URL'] = request.path_info
                return HttpResponseRedirect("/")
        return wrap
    return inner