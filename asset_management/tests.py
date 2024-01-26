# asset_management/tests.py

from django.test import TestCase
from .models import Device

class DeviceModelTest(TestCase):

    def test_device_creation(self):
        device = Device.objects.create(name='Test Device', condition='Good')
        self.assertEqual(device.name, 'Test Device')
        self.assertEqual(device.condition, 'Good')
