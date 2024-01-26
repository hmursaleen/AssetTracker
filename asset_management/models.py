# asset_management/models.py

from django.db import models
from django.contrib.auth.models import User


class AssetCategory(models.Model):
    name = models.CharField(max_length=255)

class Project(models.Model):
    name = models.CharField(max_length=255)

class Company(models.Model):
    name = models.CharField(max_length=255)



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Device(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    checked_out = models.DateTimeField(null=True, blank=True)
    returned = models.DateTimeField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(AssetCategory, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='device_images/', null=True, blank=True)


class LogEntry(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)



class AssetTransaction(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)  # "check_out" or "check_in"
    timestamp = models.DateTimeField(auto_now_add=True)




