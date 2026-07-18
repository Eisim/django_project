from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from feedback_app.forms import FeedbackForm
from feedback_app.forms import SUBJECT_CHOICES
from feedback_app.models import Feedback


class FeedbackTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='feedback_form_test_user', password='')

    def test_correct_form_creation(self):
        data_dict = {
            'name': 'koko',
            'email': 'koko@mail.ru',
            'message': 'GASG',
            'subject': SUBJECT_CHOICES[0][0],
        }
        start_feedback_len = Feedback.objects.count()

        form = FeedbackForm(data=data_dict)
        self.assertTrue(form.is_valid())

        self.client.post(reverse('feedback:feedback_page'), data_dict)

        end_feedback_len = Feedback.objects.count()
        self.assertEqual(end_feedback_len, start_feedback_len + 1)

    def test_form_validation_error(self):
        data_dict = {
            'name': 'koko',
            'eeeeemail': 'koko@mail.ru',
            'message': 'GASG',
            'subject': SUBJECT_CHOICES[0][0],
        }
        start_feedback_len = Feedback.objects.count()

        form = FeedbackForm(data=data_dict)
        self.assertFalse(form.is_valid())
        response = self.client.post(reverse('feedback:feedback_page'), data_dict)
        server_form = response.context['form']
        self.assertFalse(server_form.is_valid())
        self.assertIn('email', server_form.errors)

        end_feedback_len = Feedback.objects.count()
        self.assertEqual(end_feedback_len, start_feedback_len)
