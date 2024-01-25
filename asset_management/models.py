# asset_management/models.py

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Device(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    checked_out = models.DateTimeField(null=True, blank=True)
    returned = models.DateTimeField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
