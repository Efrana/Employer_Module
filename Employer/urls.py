from django.urls import path
from . import views
from Employer.views import Divisions, Employer_list,Employer_details

urlpatterns = [
    path('divisions/', Divisions),
    path('employer/list/', Employer_list),
    path('employer/details/', Employer_details),
]
