from django.db import models


# Create your models here.
class Account_Info(models.Model):
    username = models.CharField(max_length=200)
    email = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.username


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
    division = models.ForeignKey(Different_Ind_Type, on_delete=models.CASCADE)
    industry_type = models.OneToOneField(Industry_Type, on_delete=models.CASCADE)
    account_info = models.OneToOneField(Account_Info, on_delete=models.CASCADE)
    business_description = models.TextField()
    trade_licence_no = models.IntegerField()

    def __str__(self):
        return self.username
