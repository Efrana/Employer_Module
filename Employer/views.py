# Django Packages
import json
from pprint import pprint

from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from django.contrib.auth.models import User
# Custom App
from .models import (
    Contact,
    CompanyInfo,
    IndustryTypeMaster,
    IndustryTypeSlave,
    Thana,
    Token
)
from .helpers import json_body
from .forms import UserFrom, ContactFrom, CompanyInfoForm


# =========================================Registration================================

# Employer Registration
# http://127.0.0.1:8000/registration
@method_decorator(csrf_exempt, name='dispatch')
class EmployerRegistration(View):
    @transaction.atomic
    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_form = UserFrom(body)
        contact_form = ContactFrom(body['contact'])
        company_info = CompanyInfoForm(body['company_info'])

        if user_form.is_valid() and contact_form.is_valid() and company_info.is_valid():
            user_instance = user_form.save()

            contact_form.instance.user = user_instance
            contact_form.save()

            company_info.instance.user = user_instance
            company_info.save()
            return JsonResponse({'message': 'Registration Successful!'}, status=201)

        else:
            return JsonResponse({"errors": user_form.errors}, status=422)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateRegistration(View):
    @transaction.atomic
    def put(self, request, id=None):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            user = User.objects.get(id=id)
            print(user)
            user_form = UserFrom(body, instance=user)

            if user_form.is_valid():
                user_ins = user_form.save()

                contact = get_object_or_404(Contact, user=user_ins)
                contact_from = ContactFrom(body['contact'], instance=contact)
                contact_from.save()

                company_info = get_object_or_404(CompanyInfo, user=user_ins)
                company_from = CompanyInfoForm(body['company_info'], instance=company_info)
                company_from.save()
                return JsonResponse({'message': 'Registration Successful Updated!'}, status=200)
        except User.DoesNotExist as e:
            return JsonResponse({"message": e}, status=404)

        # else:
        #     return JsonResponse({"errors": user_form.errors}, status=422)


@method_decorator(csrf_exempt, name='dispatch')
class Authentication(View):
    def post(self, request):
        # getting api data
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user = User.objects.get(username=body['username'], password=body['password'])
        # user = authenticate(username=user_obj.username, password=user_obj.password)

        if user:
            token = generate_token()
            Token.objects.create(user=user, token=token)
            login(request, user)
            return JsonResponse({"message": f"Login successfully for {user.username}"}, status=200)
        else:
            return JsonResponse({'message': 'Login failed'}, status=204)

    def get(self, request):
        token = request.headers['Token']

        if token:
            matched_token = Token.objects.get(token=token)
            matched_token.delete()
            return JsonResponse({'message': 'Logout Successfully!'}, status=200)
        else:
            return JsonResponse({'message': 'Not Found!'}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
def logout(request):
    # getting token
    token = request.headers['Token']

    if token:
        matched_token = Token.objects.get(token=token)
        matched_token.delete()
        return JsonResponse({'message': 'Logout Successfully!'}, status=200)
    else:
        return JsonResponse({'message': 'Not Found!'}, status=404)


# custom token generating
def generate_token():
    import time

    return str(int(time.time()))
