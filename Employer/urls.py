from django.urls import path
from . import views
from Employer.views import Divisions, Employer_list, Employer_details, Signup

urlpatterns = [
    path('divisions/', Divisions),
    path('list/', Employer_list),
    path('details/<int:id>/', Employer_details),
    path('signup/', Signup)
]
