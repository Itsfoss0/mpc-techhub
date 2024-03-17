#!/usr/bin/env python3


from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        """
        Test that the home view returns a 200 status code and the expected HTML content.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1> Welcome to TechHub </h1>', html=True)
