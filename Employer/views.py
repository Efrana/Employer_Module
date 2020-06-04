from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from .models import Division, CompanyInfo, Contact, Thana,IndustryTypeSlave
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


# Create your views here.
# division API
def Divisions(request):
    context = {
        'division': list(Division.objects.values()),
    }
    return JsonResponse(context, safe=False)


# Employer list API
def Employer_list(request):
    if request.method == "GET":
        users = CompanyInfo.objects.values('name', 'b_name', 'country', 'thana__name', 'address', 'b_address',
                                           'industry_type_slave__name', 'user__username', 'business_description',
                                           'licence_no',
                                           'websiteurl')
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'company': list(page_obj),

        }
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse({'Sorry data not exist'}, status=404)


# Employer details API
def Employer_details(request, id):
    companyInfo = get_object_or_404(CompanyInfo, id=id)
    contacts = get_object_or_404(Contact, user=companyInfo.user)
    # respose_keys = [
    #     'id', 'name', 'country'
    # ]
    context = {

        'id': companyInfo.id,
        'name': companyInfo.name,
        'country': companyInfo.country,
        'thana': companyInfo.thana.name,
        'address': companyInfo.address,
        'b_address': companyInfo.b_address,
        # 'industry_type_slave':companyInfo.industry_type_slave,
        'business_description': companyInfo.business_description,
        'licence_no': companyInfo.licence_no,
        'websiteurl': companyInfo.websiteurl,
        'user': companyInfo.user.username,
        'contacts_name': contacts.name,
        'designation': contacts.designation,
        'contacts_email': contacts.email,
        'contacts_phone': contacts.phone,
    }
    return JsonResponse(context, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
@transaction.atomic
def Signup(request):
    import json
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        # User Table data
        username = body_data['username']
        email = body_data['email']
        password = body_data['password']

        # contact Table data
        name = body_data['name']
        designation = body_data['designation']
        c_email = body_data['c_email']
        phone = body_data['phone']
        userId = body_data['userId']

        # Company Table data
        c_name = body_data['c_name']
        b_name = body_data['b_name']
        country = body_data['country']
        thanaId = body_data['thanaId']
        address = body_data['address']
        b_address = body_data['b_address']
        industry_type_slave = body_data['industry_type_slave']

        business_description = body_data['business_description']
        licence_no = body_data['licence_no']
        websiteurl = body_data['websiteurl']
        # return JsonResponse(body_data, safe=False)
        # User Table Create
        if username and email and password:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )

        # Contact Table Create
        if name and designation and email and phone and user:
            contact = Contact.objects.create(
                name=name,
                designation=designation,
                email=c_email,
                phone=phone,
                user=user,
            )

        # Company Table Create
        if name and b_name and country and thanaId and address and b_address and industry_type_slave and user and business_description and licence_no and websiteurl:
            company = CompanyInfo.objects.create(
                name=c_name,
                b_name=b_name,
                country=country,
                thana=get_object_or_404(Thana, id=thanaId),
                address=address,
                b_address=b_address,
                industry_type_slave=industry_type_slave,
                user=user,
                business_description=business_description,
                licence_no=licence_no,
                websiteurl=websiteurl,

            )
            # company.industry_type_slave.add(IndustryTypeSlave_request.get("industry_type_slave"))

        return JsonResponse('successfully registered!', safe=False)
    else:
        return JsonResponse('Failed!', safe=False)
