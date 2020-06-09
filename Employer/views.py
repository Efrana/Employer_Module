from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from .models import Division, CompanyInfo, Contact, Thana, IndustryTypeSlave
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
        queryset = CompanyInfo.objects.prefetch_related('industry_type_slave')
        companys = []

        for company in queryset:
            industry_type_slave = [company.name for company in company.industry_type_slave.all()]
            companys.append(
                {'id': company.id, 'name': company.name, 'b_name': company.b_name, 'country': company.country,
                 'thana': company.thana.name,
                 'address': company.address, 'b_address': company.b_address,
                 'industry_type_slave': industry_type_slave, 'user': company.user.username,
                 'business_description': company.business_description, 'licence_no': company.licence_no,
                 'websiteurl': company.websiteurl})

        paginator = Paginator(companys, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'company': list(page_obj),

            'pagination': {
                'total_pages': page_obj.paginator.num_pages,
                'current_page_number': page_obj.number,
                'previous': page_obj.has_previous() > 0 and page_obj.previous_page_number() or None,
                'next': page_obj.has_next() > 0 and page_obj.next_page_number() or None
            }
        }
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse('Sorry data not exist', status=404)


#####################################################
# Employer details API
def Employer_details(request, id):
    if request.method == "GET":
        queryset = CompanyInfo.objects.prefetch_related('industry_type_slave').get(id=id)
        contacts = get_object_or_404(Contact, user=queryset.user)

        companys = []

        industry_type_slave = [company.name for company in queryset.industry_type_slave.all()]
        companys.append(
            {'id': queryset.id, 'name': queryset.name, 'b_name': queryset.b_name, 'country': queryset.country,
             'thana': queryset.thana.name, 'district': queryset.thana.district.name,
             'division': queryset.thana.district.division.name,
             'address': queryset.address, 'b_address': queryset.b_address,
             'industry_type_slave': industry_type_slave, 'user': queryset.user.username,
             'business_description': queryset.business_description, 'licence_no': queryset.licence_no,
             'websiteurl': queryset.websiteurl, 'contacts_name': contacts.name, 'designation': contacts.designation,
             'contacts_email': contacts.email, 'contacts_phone': contacts.phone})
        context = {
            'company': list(companys),

        }
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse('Sorry data not exist', status=404)

###########################################################################################

# Employer details API
# def Employer_details(request, id):
#     companyInfo = get_object_or_404(CompanyInfo, id=id)
#     contacts = get_object_or_404(Contact, user=companyInfo.user)
#     context = {
#
#         'id': companyInfo.id,
#         'name': companyInfo.name,
#         'country': companyInfo.country,
#         'thana': companyInfo.thana.name,
#         'district': companyInfo.thana.district.name,
#         'division': companyInfo.thana.district.division.name,
#         'address': companyInfo.address,
#         'b_address': companyInfo.b_address,
#         # 'industry_type_slave':list(companyInfo.industry_type_slave),
#         'business_description': companyInfo.business_description,
#         'licence_no': companyInfo.licence_no,
#         'websiteurl': companyInfo.websiteurl,
#         'user': companyInfo.user.username,
#         'contacts_name': contacts.name,
#         'designation': contacts.designation,
#         'contacts_email': contacts.email,
#         'contacts_phone': contacts.phone,
#     }
#     return JsonResponse(context, safe=False)
