from django.contrib import admin

# Register your models here.

from .models import Company, Employee, Device

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
