from django.contrib import admin

from .models import (
    Contact,
    CompanyInfo,
    IndustryTypeMain,
    IndustryTypeSubordinate,
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
    list_display = ['name', 'b_name', 'thana', 'address', 'business_description', 'user', 'get_industry_type_subordinate']


# industry type main table
@admin.register(IndustryTypeMain)
class IndustrytypemainAdmin(admin.ModelAdmin):
    list_display = ['name']


# IndustryTypeSubordinate table
@admin.register(IndustryTypeSubordinate)
class IndustrytypesubordinateAdmin(admin.ModelAdmin):
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
