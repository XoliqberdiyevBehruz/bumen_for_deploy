from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestCategoryAPIView(APITestCase):
    def setUp(self):
        pass

    def test_happy(self):
        url = reverse('category-subject')
        data = {
            "question": "Test_question",
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['question'], 'Test_question')
        self.assertEquals(list(response.data.keys()), ['question'])

