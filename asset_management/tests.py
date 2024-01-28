# asset_management/tests.py

from django.test import TestCase
from .models import Device, Company, Employee, AssetCategory, Project
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import DeviceSerializer


class DeviceModelTest(TestCase):

    def setUp(self):
        company = Company.objects.create(name='Test Company')
        employee = Employee.objects.create(name='Test Employee', company=company)
        category = AssetCategory.objects.create(name='Test Category')
        project = Project.objects.create(name='Test Project')

        self.device = Device.objects.create(
            name='Test Device',
            condition='Good',
            employee=employee,
            category=category,
            project=project,
        )

    def test_device_creation(self):
        self.assertEqual(self.device.name, 'Test Device')
        self.assertEqual(self.device.condition, 'Good')
        self.assertEqual(str(self.device), 'Test Device')  # Test __str__ method
        self.assertIsNotNone(self.device.checked_out)

    def test_device_return(self):
        self.device.returned = self.device.checked_out + timedelta(days=7)
        self.device.save()
        self.assertIsNotNone(self.device.returned)






class DeviceAPITestCase(APITestCase):

    def setUp(self):
        company = Company.objects.create(name='Test Company')
        employee = Employee.objects.create(name='Test Employee', company=company)
        category = AssetCategory.objects.create(name='Test Category')
        project = Project.objects.create(name='Test Project')

        self.device_data = {
            'name': 'Test Device',
            'condition': 'Good',
            'employee': employee.id,
            'category': category.id,
            'project': project.id,
        }

    def test_create_device(self):
        response = self.client.post('/api/devices/', data=self.device_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.objects.count(), 1)

    def test_device_serializer_validation(self):
        # Test validation errors for missing required fields
        invalid_data = {}
        serializer = DeviceSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
        self.assertIn('condition', serializer.errors)
        self.assertIn('employee', serializer.errors)
        self.assertIn('category', serializer.errors)

    def test_device_serializer_representation(self):
        device = Device.objects.create(**self.device_data)
        serializer = DeviceSerializer(device)
        expected_data = {
            'id': device.id,
            'name': 'Test Device',
            'condition': 'Good',
            'employee': device.employee.id,
            'category': device.category.id,
            'project': device.project.id,
            'checked_out': serializer.data['checked_out'],  # Assuming checked_out is present in the representation
            'returned': serializer.data['returned'],
            'image': serializer.data['image'],  # Assuming image is present in the representation
        }
        self.assertEqual(serializer.data, expected_data)





class DeviceAPITestCase(APITestCase):

    def setUp(self):
        company = Company.objects.create(name='Test Company')
        employee = Employee.objects.create(name='Test Employee', company=company)
        category = AssetCategory.objects.create(name='Test Category')
        project = Project.objects.create(name='Test Project')

        self.device_data = {
            'name': 'Test Device',
            'condition': 'Good',
            'employee': employee.id,
            'category': category.id,
            'project': project.id,
        }

        self.device = Device.objects.create(**self.device_data)

    def test_get_device_list(self):
        response = self.client.get('/api/devices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_device_detail(self):
        response = self.client.get(f'/api/devices/{self.device.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Device')

    def test_update_device(self):
        updated_data = {
            'name': 'Updated Device',
            'condition': 'Fair',
            'employee': self.device.employee.id,
            'category': self.device.category.id,
            'project': self.device.project.id,
        }

        response = self.client.put(f'/api/devices/{self.device.id}/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.device.refresh_from_db()
        self.assertEqual(self.device.name, 'Updated Device')

    def test_delete_device(self):
        response = self.client.delete(f'/api/devices/{self.device.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Device.objects.count(), 0)
