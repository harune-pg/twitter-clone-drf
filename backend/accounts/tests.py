from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# from .factories import UserFactory


User = get_user_model()

class SignupAPIViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('accounts:signup')

    def test_success_signup(self):
        valid_data = {
            "username": "testuser",
            "password": "testpassword",
            "re_password": "testpassword",
        }
        response = self.client.post(self.url, valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")


# class LoginTests(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = UserFactory(password="testpassword")

#     def setUp(self):
#         self.url = reverse('accounts:login')

#     def test_success_login(self):
#         valid_data = {
#             "username": self.user.username,
#             "password": "testpassword",
#         }
#         response = self.client.post(self.url, valid_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('access', response.cookies)
#         self.assertIn('refresh', response.cookies)
#         self.assertEqual(response.data['user']['username'], self.user.username)


# class LogoutViewTests(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = UserFactory()

#     def setUp(self):
#         self.url = reverse('accounts:logout')
#         self.client.force_authenticate(user=self.user)

#     def test_success_logout(self):
#         response = self.client.post(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.cookies.get('access').value, '')
#         self.assertEqual(response.cookies.get('refresh').value, '')
