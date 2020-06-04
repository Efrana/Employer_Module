from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'email', 'phone', 'user']


admin.site.register(Contact, ContactAdmin)


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Division, DivisionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'division']


admin.site.register(District, DistrictAdmin)


class ThanaAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']


admin.site.register(Thana, ThanaAdmin)


class IndustryTypeMasterAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(IndustryTypeMaster, IndustryTypeMasterAdmin)


class IndustryTypeSlaveAdmin(admin.ModelAdmin):
    list_display = ['name', 'industry_type_master']


admin.site.register(IndustryTypeSlave, IndustryTypeSlaveAdmin)


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name','b_name' ,'country', 'thana', 'address','b_address', 'get_industry_type_slave', 'user', 'business_description',
                    'licence_no', 'websiteurl']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
