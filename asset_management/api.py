# asset_management/api.py

from rest_framework import viewsets
from .models import Company, Employee, AssetCategory, Project, Device, AssetTransaction
from .serializers import CompanySerializer, EmployeeSerializer, AssetCategorySerializer, \
    ProjectSerializer, DeviceSerializer, AssetTransactionSerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'condition', 'checked_out', 'returned', 'employee__name', 'category__name']


class AssetTransactionViewSet(viewsets.ModelViewSet):
    queryset = AssetTransaction.objects.all()
    serializer_class = AssetTransactionSerializer
