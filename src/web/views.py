#!/usr/bin/env python3


"""
Views for the web app
"""

from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1> Welcome to TechHub </>")