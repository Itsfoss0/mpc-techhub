#!/usr/bin/env python3


"""
URL configuration for the /api/v1 endpoints
"""

from django.urls import path
from api.views import ping


urlpatterns = [
    path('status', ping, name='ping')
]
