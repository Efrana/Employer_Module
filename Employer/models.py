from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Contact(models.Model):
    person_name = models.CharField(max_length=200)
    person_designation = models.CharField(max_length=200)
    person_email = models.CharField(max_length=200)
    person_phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Division(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DifferentIndType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IndustryType(models.Model):
    name = models.CharField(max_length=200)
    different_ind_type = models.ForeignKey(DifferentIndType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CompanyInfo(models.Model):
    company_name=models.CharField(max_length=200,default=None, blank=True)
    country = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    industry_type = models.OneToOneField(IndustryType, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_description = models.TextField()
    trade_licence_no = models.IntegerField()

    def __str__(self):
        return self.user.username





