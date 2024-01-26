# asset_management/serializers.py

from rest_framework import serializers
from .models import Company, Employee, AssetCategory, Project, Device, AssetTransaction

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class AssetTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetTransaction
        fields = '__all__'
