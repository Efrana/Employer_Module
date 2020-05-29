from django.contrib import admin
from .models import *


# Register your models here.

# class Account_InfoAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'password']
#
#
# admin.site.register(Account_Info, Account_InfoAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'person_designation', 'person_email', 'person_phone', 'user']


admin.site.register(Contact, ContactAdmin)


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Division, DivisionAdmin)


class DifferentIndTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(DifferentIndType, DifferentIndTypeAdmin)


class IndustryTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'different_ind_type']


admin.site.register(IndustryType, IndustryTypeAdmin)


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name','country', 'division', 'industry_type', 'user', 'business_description', 'trade_licence_no']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
