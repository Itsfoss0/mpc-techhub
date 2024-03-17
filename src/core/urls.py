#!/usr/bin/env python3


"""
Main url conf
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web.urls')),
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
]
