from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=250)

    def __str__(self):
        return str(self.token)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Division(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Thana(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IndustryTypeMaster(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IndustryTypeSlave(models.Model):
    name = models.CharField(max_length=200)
    industry_type_master = models.ForeignKey(IndustryTypeMaster, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    b_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    thana = models.ForeignKey(Thana, on_delete=models.CASCADE)
    address = models.TextField()
    b_address = models.TextField()
    industry_type_slave = models.ManyToManyField(IndustryTypeSlave, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_description = models.TextField()
    licence_no = models.IntegerField()
    websiteurl = models.URLField(max_length=350)

    def __str__(self):
        return self.user.username

    def thana_name(self):
        return self.thana.name

    def industry_type_slave_name(self):
        return self.industry_type_slave.name

    def get_industry_type_slave(self):
        return ",".join([str(p) for p in self.industry_type_slave.all()])
