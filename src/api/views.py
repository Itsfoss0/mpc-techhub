#!/usr/bin/env python3
"""
Views for the /api/v1 endpoint 
"""

from django.http import JsonResponse, HttpRequest


def ping(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "OK"})
