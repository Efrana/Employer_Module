from django.contrib import admin

from .models import (
    Contact,
    CompanyInfo,
    IndustryTypeMaster,
    IndustryTypeSlave,
    Division,
    District,
    Thana,
    Token
)


# Toke table
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'token']


# Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation', 'contact_email', 'phone', 'user']
    list_display_links = ['name']
    search_fields = ['name', 'designation', 'contact_email', 'phone', 'user']
    list_filter = ['id', 'name', 'designation', 'contact_email', 'phone', 'user']


# company info table
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'b_name', 'thana', 'address', 'business_description', 'user']


# industry type master table
@admin.register(IndustryTypeMaster)
class IndustrytypemasterAdmin(admin.ModelAdmin):
    list_display = ['name']


# IndustryTypeSlave table
@admin.register(IndustryTypeSlave)
class IndustrytypeslaveAdmin(admin.ModelAdmin):
    list_display = ['name']


# Division table
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']


# Districts table
@admin.register(District)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']


# Thana table
@admin.register(Thana)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name']
