from django.urls import path

# custom app
from .views import (

    EmployerRegistration,
    Authentication
    # UpdateRegistration,
    # LoginLogout
)

urlpatterns = [

    # sign-up api
    path('registration/', EmployerRegistration.as_view()),
    path('registration-update/', EmployerRegistration.as_view()),
    # login logout
    path('authentication/', Authentication.as_view()),
    # edit
    path('authentication/<int:id>/', Authentication.as_view()),
    # path('employer/logout/', logout),

]
