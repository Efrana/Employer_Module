from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account_Info(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.TextField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username.username


class Contact(models.Model):
    person_name = models.CharField(max_length=200)
    person_designation = models.CharField(max_length=200)
    person_email = models.CharField(max_length=200)
    person_phone = models.IntegerField()
    account_info = models.OneToOneField(Account_Info, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Different_Ind_Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Industry_Type(models.Model):
    name = models.CharField(max_length=200)
    different_ind_type = models.ForeignKey(Different_Ind_Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Company_Info(models.Model):
    country = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    industry_type = models.OneToOneField(Industry_Type, on_delete=models.CASCADE)
    account_info = models.OneToOneField(Account_Info, on_delete=models.CASCADE)
    business_description = models.TextField()
    trade_licence_no = models.IntegerField(max_length=25)

    def __str__(self):
        return self.username