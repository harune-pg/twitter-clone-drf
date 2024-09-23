from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SampleAPIViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('sample')

    def test_success_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Hellow, World")
