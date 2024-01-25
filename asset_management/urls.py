# asset_management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CompanyViewSet, EmployeeViewSet, DeviceViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Add the following for documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Asset Tracking API",
        default_version='v1',
        description="API for tracking corporate assets",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
