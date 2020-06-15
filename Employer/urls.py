from django.urls import path

# custom app
from .views import (

    EmployerRegistration,
    Authentication,
    UpdateRegistration,
    logout
)

urlpatterns = [


  # sign-up api
    path('employer/registration/', EmployerRegistration.as_view()),
    path('employer/registration-update/<int:id>/', UpdateRegistration.as_view()),
    # login logout
    path('authentication/', Authentication.as_view()),
    path('employer/logout/', logout),

]
