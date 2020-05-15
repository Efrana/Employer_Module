from django.contrib import admin
from .models import *


# Register your models here.

class Account_InfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']


admin.site.register(Account_Info, Account_InfoAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'person_designation', 'person_email', 'person_phone', 'account_info']


admin.site.register(Contact, ContactAdmin)


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Division, DivisionAdmin)


class Different_Ind_TypeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Different_Ind_Type, Different_Ind_TypeAdmin)


class Industry_TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'different_ind_type']


admin.site.register(Industry_Type, Industry_TypeAdmin)


class Company_InfoAdmin(admin.ModelAdmin):
    list_display = ['country', 'division', 'industry_type', 'account_info', 'business_description', 'trade_licence_no']


admin.site.register(Company_Info, Company_InfoAdmin)
