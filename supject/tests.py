from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from supject.models import *


class SubmitTestViewTest(APITestCase):
    def setUp(self):
        self.test_question_1 = TestQuestion.objects.create(
            question_type='single',
            question='Test Question 1',
            level=TestQuestion.QuestionLevel.EASY
        )
        self.test_question_2 = TestQuestion.objects.create(
            question_type='single',
            question='Test Question 2',
            level=TestQuestion.QuestionLevel.MEDIUM
        )

    def test_submit_test_view(self):
        url = reverse('submit-test')
        data = {
            "step_id": self.step.id
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("result_id", response.data)
        self.assertIn("questions", response.data)
        self.assertEqual(len(response.data["questions"]), 2)

