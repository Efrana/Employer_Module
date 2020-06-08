from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods

# auth user model
from django.contrib.auth.models import User
from .models import (
    CompanyInfo,
    Contact,
    IndustryType,
    DifferentIndType,
    Division
)


# Create your views here.
# signup api
@csrf_exempt
@require_http_methods(["POST"])
def sign_up(request):
    # getting api data
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    # if data available
    if username and email and password:
        # user creation
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        # contact table
        # getting api data
        person_name = request.POST.get('person_name')
        person_designation = request.POST.get('person_designation')
        person_email = request.POST.get('person_email')
        person_phone = request.POST.get('person_phone')

        # contact creation
        contact = Contact.objects.create(
            person_name=person_name,
            person_designation=person_designation,
            person_email=person_email,
            person_phone=person_phone,
            user=user
        )
        # modifying data to json format

        # company info
        # getting api data
        company_name = request.get('company_name')
        country = request.POST.get('country')
        division = request.POST.get('division')
        industry_type = request.POST.get('industry_type')
        business_description = request.POST.get('business_description')
        trade_licence_no = request.POST.get('trade_licence_no')

        # company info creation
        company_info = CompanyInfo.objects.create(
            company_name=company_name,
            country=country,
            division=division,
            industry_type=industry_type,
            business_description=business_description,
            trade_licence_no=trade_licence_no,
            user=user
        )

        # return api response
        return JsonResponse({'message': 'Employer successfully register done!'}, status=201)

    # if data not available
    else:
        return JsonResponse({'message': 'Signup Failed!'}, status=404)


# login api
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    # getting api data
    username = request.POST.get('username')
    password = request.POST.get('password')

    # if data available
    if username and password:

        # checking
        authenticated = authenticate(username=username, password=password)

        # if authenticated user
        if authenticated:

            # if succeed
            return JsonResponse({'authenticated': 'Login successfully done'}, status=200)

        # if not succeed
        else:
            return JsonResponse({'message': 'Login Failed!'}, status=401)

    # if data not available
    else:
        return JsonResponse({'message': 'Not Found!'}, status=404)

# logout api

@csrf_exempt
@require_http_methods(["POST"])
def logout(request):
    id = request.POST.get('id')
    if id:
        user =User.objects.get(id=id)
        logout(request)
        # user.delete()
        return JsonResponse({'message': 'Logout Successfully!'}, status=200)
    else:
        return JsonResponse({'message': 'Not Found!'}, status=404)



