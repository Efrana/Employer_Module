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
        fields = ['name', 'b_name', 'country' , 'address' , 'b_address', 'industry_type_slave', 'business_description', 'licence_no', 'websiteurl']
        exclude = ['user' , 'name', 'thana']
        # name = models.CharField(max_length=200)
        # b_name = models.CharField(max_length=200)
        # country = models.CharField(max_length=200)
        # thana = models.ForeignKey(Thana, on_delete=models.CASCADE)
        # address = models.TextField()
        # b_address = models.TextField()
        # industry_type_slave = models.ManyToManyField(IndustryTypeSlave)
        # user = models.OneToOneField(User, on_delete=models.CASCADE)
        # business_description = models.TextField()
        # licence_no = models.IntegerField()
        # websiteurl = models.URLField(max_length=350)
