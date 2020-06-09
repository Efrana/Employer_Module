# Django Packages
import json
from pprint import pprint

from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
# Custom App
from .models import (
    Contact,
    CompanyInfo,
    IndustryTypeMaster,
    IndustryTypeSlave,
    Thana
)
from .helpers import json_body
from .forms import UserFrom, ContactFrom, CompanyInfoFrom


# =========================================Registration================================

# JobSeeker Registration
# http://127.0.0.1:8000/registration
@method_decorator(csrf_exempt, name='dispatch')
class EmployerRegistration(View):
    # user_fields = ['username', 'email', 'password', 'name', 'designation', 'contact_email', 'phone']

    def post(self, request):
        # user_form = UserFrom(json_body(request))

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user_form = UserFrom(body)

        if user_form.is_valid():
            user_instance = user_form.save()

            # contact table
            contact_form = ContactFrom(body)
            contact_form.instance.user = user_instance
            print(contact_form.instance.user)
            contact_form_instance = contact_form.save()

            # company_info table
            company_info = CompanyInfoFrom(body)
            print('51', company_info)
            company_info.instance.user = user_instance
            print('54')
            company_info.instance.thana = Thana.objects.get(id=company_info.thana)
            print('56', company_info.instance.thana)
            company_info.industry_type_slave = IndustryTypeSlave.objects.get(id=company_info.industry_type_slave)

            company_info.save()
            return JsonResponse(model_to_dict(contact_form_instance,
                                              fields=[field.name for field in contact_form_instance._meta.fields]))
            # return JsonResponse(model_to_dict(contact_form_instance, fields=self.user_fields))
            # else:
            #     return JsonResponse({"errors": "failed"}, status=422)

        else:
            return JsonResponse({"errors": user_form.errors.as_json()}, status=422)

        # contact_from = ContactFrom(json_body(request))
        # print(contact_from)
        # if contact_from.is_valid():
        #     contact_from.instance.save(user=user_form)
    #     return JsonResponse({'message': 'Registration Successful!'}, status=201)
    # else:
    #     return JsonResponse({'message': user_form.errors}, status=422)
#
# # auth user model
# from django.contrib.auth.models import User
# from .models import (
#     CompanyInfo,
#     Contact,
#     IndustryType,
#     DifferentIndType,
#     Division
# )
#
#
# # Create your views here.
# # signup api
# @csrf_exempt
# @require_http_methods(["POST"])
# @transaction.atomic
# def sign_up(request):
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#
#     # getting api data
#     username = body['username']
#     email = body['email']
#     password = body['password']
#
#     # if data available
#     if username and email and password:
#         # user creation
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#         )
#
#         # contact table
#         # getting api data
#         person_name = body['person_name']
#         person_designation = body['person_designation']
#         person_email = body['person_email']
#         person_phone = body['person_phone']
#
#         # contact creation
#         contact = Contact.objects.create(
#             person_name=person_name,
#             person_designation=person_designation,
#             person_email=person_email,
#             person_phone=person_phone,
#             user=user
#         )
#
#         # company info
#         # getting api data
#         company_name = body['company_name']
#         country = body['country']
#         division = body['division']
#         industry_type = body['industry_type']
#         business_description = body['business_description']
#         trade_licence_no = body['trade_licence_no']
#
#         # company info creation
#         company_info = CompanyInfo.objects.create(
#             company_name=company_name,
#             country=country,
#             division=Division.objects.get(id=division),
#             industry_type=IndustryType.objects.get(id=industry_type),
#             business_description=business_description,
#             trade_licence_no=trade_licence_no,
#             user=user
#         )
#
#         # return api response
#         return JsonResponse({'message': 'Employer successfully register done!'}, status=201)
#
#     # if data not available
#     else:
#         return JsonResponse({'message': 'Signup Failed!'}, status=404)
#
#
# # login api
# @csrf_exempt
# @require_http_methods(["POST"])
# def login(request):
#     # getting api data
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#
#     username = body['username']
#     password = body['password']
#
#     # if data available
#     if username and password:
#
#         # checking
#         authenticated = authenticate(username=username, password=password)
#
#         # if authenticated user
#         if authenticated:
#
#             # if succeed
#             return JsonResponse({'authenticated': 'Login successfully done'}, status=200)
#
#         # if not succeed
#         else:
#             return JsonResponse({'message': 'Login Failed!'}, status=401)
#
#     # if data not available
#     else:
#         return JsonResponse({'message': 'Not Found!'}, status=404)
#
#
# # logout api
#
# @csrf_exempt
# @require_http_methods(["POST"])
# def logout(request):
#     id = request.POST.get('id')
#     if id:
#         user = User.objects.get(id=id)
#         logout(user)
#         # user.delete()
#         return JsonResponse({'message': 'Logout Successfully!'}, status=200)
#     else:
#         return JsonResponse({'message': 'Not Found!'}, status=404)
#
#
# @csrf_exempt
# @require_http_methods(["POST"])
# @transaction.atomic
# def update(request, id=None):
#     # receving API data
#     try:
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#
#         # getting api data
#         username = body['username']
#         email = body['email']
#         user = get_object_or_404(User, id=id)
#         print(user)
#         user.username = username
#         user.email = email
#         user.save()
#
#         person_name = body['person_name']
#         person_designation = body['person_designation']
#         person_email = body['person_email']
#         person_phone = body['person_phone']
#         company_name = body['company_name']
#         country = body['country']
#         division = body['division']
#         industry_type = body['industry_type']
#         business_description = body['business_description']
#         trade_licence_no = body['trade_licence_no']
#
#         contact = get_object_or_404(Contact, user=user)
#         print(contact)
#         contact.person_name = person_name
#         # print(user.person_name)
#         contact.person_designation = person_designation
#         contact.person_email = person_email
#         contact.person_phone = person_phone
#         contact.save()
#
#         company_info = get_object_or_404(CompanyInfo, user=user)
#         print(company_info)
#         company_info.company_name = company_name
#         company_info.country = country
#         company_info.division = Division.objects.get(id=division)
#         company_info.industry_type = IndustryType.objects.get(id=industry_type)
#         company_info.business_description = business_description
#         company_info.trade_licence_no = trade_licence_no
#         company_info.save()
#
#         return JsonResponse({"message": "Updated!"}, status=201, safe=False)
#
#     except User.DoesNotExist as e:
#         return JsonResponse({"message": e}, status=404, safe=False)
#
#
