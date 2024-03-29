# asset_tracking/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('asset_management.urls')),
    path('', include('asset_management.urls')),
]
