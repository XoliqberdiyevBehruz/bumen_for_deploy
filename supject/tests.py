from unicodedata import category
from django.test import TestCase
from django.urls import reverse
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
        

class TestSubjectView(APITestCase):
    def setUp(self):
        
        self.category1 = Category.objects.create(name="Category1", click_count=1)
        self.user1 = User.objects.create_user(email='user@example.com', password='password')
        
        self.category2 = Category.objects.create(name="Category2", click_count=2)
        self.user2 = User.objects.create_user(email='user@example2.com', password='password')
        
        SubjectTitle.objects.create(name=self.user1, category=self.category1)
        SubjectTitle.objects.create(name=self.user2, category=self.category2)
        
    def test_happy(self):
        url = reverse("subject-search")
        test_query = "Category1"
        response = self.client.get(f"{url}?query={test_query}", format='json')
        count = SubjectTitle.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 2)