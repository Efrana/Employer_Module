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
        fields = ['username', 'email', 'password']


# Contact Form
class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'designation', 'contact_email', 'phone']
        exclude = ['user']


# CompanyInfo Form
class CompanyInfoFrom(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
