#!/usr/bin/env python3

"""
Test for the API
"""

from django.test import TestCase, Client
from django.urls import reverse

class PingViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ping_view(self):
        """
        Test that the ping view returns a 200 status code and the expected response.
        """
        url = reverse('ping')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'OK'})