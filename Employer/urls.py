from django.urls import path

# custom app
from .views import *


urlpatterns = [

    # sign-up api
    path('registration/', EmployerRegistration.as_view()),
    # path('employer/login/', login),
    # path('employer/logout/', logout),



]