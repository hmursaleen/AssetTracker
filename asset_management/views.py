# asset_management/views.py

from rest_framework import generics
from .models import Company, Employee, Device
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer
from .api import CompanyViewSet, EmployeeViewSet, DeviceViewSet

# Define any additional views if needed
