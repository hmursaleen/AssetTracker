# asset_management/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from asset_management.api import CompanyViewSet, EmployeeViewSet, AssetCategoryViewSet, \
    ProjectViewSet, DeviceViewSet, AssetTransactionViewSet, UserViewSet

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

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'asset-categories', AssetCategoryViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'asset-transactions', AssetTransactionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
