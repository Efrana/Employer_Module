from django.contrib import admin

from .models import (
    Contact,
    CompanyInfo,
    IndustryTypeMaster,
    IndustryTypeSlave,
    Division,
    District,
    Thana,
)


# Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','designation','contact_email','phone','user']
    list_display_links = ['name']
    search_fields = ['name','designation','contact_email','phone','user']
    list_filter = ['id', 'name','designation','contact_email','phone','user']

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'b_name', 'thana', 'address', 'business_description']

@admin.register(IndustryTypeMaster)
class IndustrytypemasterAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(IndustryTypeSlave)
class IndustrytypeslaveAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']