from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Subject, SubjectTitle


class CategoryListViewTests(APITestCase):

    def setUp(self):
        # Create test data
        self.category = Category.objects.create(name="Test Category", click_count=10)
        self.subject_title = SubjectTitle.objects.create(
            name="Test Subject Title", category=self.category
        )
        self.subject = Subject.objects.create(
            name="Test Subject",
            type=Subject.SubjectType.LOCAL,
            subject_title=self.subject_title,
        )

    def test_get_categories(self):
        url = reverse("categories")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Category")
        self.assertEqual(response.data[0]["click_count"], 10)
        # self.assertEqual(response.data[0]['subject_titles'][0]['name'], 'Test Subject Title')
        # self.assertEqual(len(response.data[0]['subject_titles'][0]['subjects']), 1)
        # self.assertEqual(response.data[0]['subject_titles'][0]['subjects'][0]['name'], 'Test Subject')
        # self.assertEqual(response.data[0]['subject_titles'][0]['subjects'][0]['type'], 'local')
