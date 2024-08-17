from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from account.models import User
from supject.models import Subject
from .models import UserSubject, SubjectTitle, Category


class TestUserPopularSubject(APITestCase):
    def setUp(self):
        self.url = reverse('userpopularsubject')
        category = Category.objects.create(name="Category 1")
        subject_title = SubjectTitle.objects.create(name="Subject Title 1", category=category)

        self.subject1 = Subject.objects.create(name="Subject 1", type='local', subject_title=subject_title)
        self.subject2 = Subject.objects.create(name="Subject 2", type='global', subject_title=subject_title)

        self.user = User.objects.create_user(email='user@example.com', password='password')
        
        UserSubject.objects.create(user=self.user, subject=self.subject1, started=True)
        UserSubject.objects.create(user=self.user, subject=self.subject2, started=True)

    def test_happy(self):
        response = self.client.get(self.url)
        print(f"URL: {self.url}")
        print(f"Response Status Code: {response.status_code}")

        if response.status_code == 404:
            print(f"Response Content: {response.content.decode('utf-8')}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        expected_data = [
            {
                'id': self.subject1.id,
                'name': 'Subject 1',
                'type': 'local',
                'subject_title': self.subject1.subject_title.id,
                'steps': [],
                'start_count': 1
            },
            {
                'id': self.subject2.id,
                'name': 'Subject 2',
                'type': 'global',
                'subject_title': self.subject2.subject_title.id,
                'steps': [],
                'start_count': 1
            },
        ]
        
        self.assertEqual(response.data, expected_data)