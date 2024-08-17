from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class TestContactWithUsView(APITestCase):

    def setUp(self):
        pass

    def test_happy(self):
        url = reverse("contact_with_us")
        data = {
            "name": "TestName",
            "phone_number": "+998919209292",
            "message": "TestMesssage",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "TestName")
        self.assertEqual(
            list(response.data.keys()), ["name", "phone_number", "message"]
        )
