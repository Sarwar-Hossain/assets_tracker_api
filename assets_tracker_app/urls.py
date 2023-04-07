from django.urls import path, include
from assets_tracker_app.views import *


urlpatterns = [
    path('login/', CompanyLoginView.as_view(), name='company-login'),
    path('', CompanyAV.as_view(), name='company'),
    path('api/company/<int:pk>/', CompanyDetailsAV.as_view(), name='company_details'),
    path('api/device/entry/', DeviceAV.as_view(), name='device'),
    path('api/device/<int:pk>/', DeviceDetailsAV.as_view(), name='device_details'),
    path('api/employee/', EmployeeAV.as_view(), name='employee'),
    path('api/employee/<int:pk>/', EmployeeDetailsAV.as_view(), name='device_details'),
    path('api/device/log/', DeviceLogAV.as_view(), name='device_log'),
    path('api/device/log/<int:pk>/', DeviceLogDetailsAV.as_view(), name='device_log_details'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
