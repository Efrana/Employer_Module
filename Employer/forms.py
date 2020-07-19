from django import forms
from django.contrib.auth.models import User

# Custom App
from .models import (
    Contact,
    CompanyInfo,
)


# user Form
class UserFrom(forms.ModelForm):
    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'password', ]


# # user Form
# class LoginFrom(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username' 'password']


# Contact Form
class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'designation', 'contact_email', 'phone']
        exclude = ['user']


# CompanyInfo Form
class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = ['name', 'b_name', 'country', 'thana', 'address', 'b_address', 'business_description',
                  'industry_type_subordinate', 'licence_no', 'websiteurl']
        exclude = ['user']
