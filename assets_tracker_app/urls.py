from django.contrib import admin
from django.urls import path, include
from assets_tracker_app.views import *


urlpatterns = [
    path('', CompanyAV.as_view(), name='company'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

