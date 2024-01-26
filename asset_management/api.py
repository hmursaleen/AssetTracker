# asset_management/api.py

from rest_framework import viewsets
from .models import Company, Employee, AssetCategory, Project, Device, AssetTransaction
from .serializers import CompanySerializer, EmployeeSerializer, AssetCategorySerializer, \
    ProjectSerializer, DeviceSerializer, AssetTransactionSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AssetTransactionViewSet(viewsets.ModelViewSet):
    queryset = AssetTransaction.objects.all()
    serializer_class = AssetTransactionSerializer
