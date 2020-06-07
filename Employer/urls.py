from django.urls import path

# custom app
from .views import *


urlpatterns = [

    # sign-up api
    path('employer/sign-up/', sign_up),



]