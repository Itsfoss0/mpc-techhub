#!/usr/bin/env python3


"""
URL configs for the web endpoints
"""

from django.urls import path
from web.views import home


urlpatterns = [
    path('', home, name='home')
]

