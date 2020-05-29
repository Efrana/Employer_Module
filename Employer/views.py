from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Division, CompanyInfo
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def Divisions(request):
    context = {
        'division': list(Division.objects.values()),
    }
    return JsonResponse(context, safe=False)


def Employer_list(request):
    context = {
        'username': list(User.objects.values('id', 'username')),
    }
    return JsonResponse(context, safe=False)


def Employer_details(request):
    context = {
        'company_info': list(CompanyInfo.objects.all().values()),
    }
    return JsonResponse(context, safe=False)

#
# @csrf_exempt
# @require_http_methods(["POST"])
# def Registration(request):
#     import json
#     if request.method == 'POST':
#         # body_unicode = request.body.decode('utf-8')
#         # body_data = json.loads(body_unicode)
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#         )
#         user_data = {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email
#         }
#         return JsonResponse(user_data, safe=False)
#     else:
#         return JsonResponse('Failed!', safe=False)
