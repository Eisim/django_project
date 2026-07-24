from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse

from users_app.models import Profile


class ProfileTest(TestCase):
    # def setUp(self):
    #     ...

    def test_create_new_profile_from_user(self):
        new_user = User.objects.create_user(username='feedback_form_test_user', password='')
        profile_created = Profile.objects.filter(pk=new_user.pk).exists()
        self.assertTrue(profile_created)

    def test_anonymous_edit_profile_redirect(self):
        """Правильное поведение: незарегистрированный пользователь не может зайти на страницу редактирования для всех профилей"""
        new_user = User.objects.create_user(username='feedback_form_test_user', password='')
        profile = Profile.objects.get(pk=new_user.pk)
        response = self.client.get(reverse('users:update', kwargs={'pk': profile.pk}))
        self.assertEqual(response.status_code, 403)

    def test_logged_user_can_edit_his_profile(self):
        new_user = User.objects.create_user(username='feedback_form_test_user', password='')
        profile = Profile.objects.get(pk=new_user.pk)
        self.client.login(username='feedback_form_test_user', password='')
        response = self.client.get(reverse('users:update', kwargs={'pk': profile.pk}))
        self.assertEqual(response.status_code, 200)

    def test_logged_user_cannot_edit_another_profile(self):
        User.objects.create_user(username='feedback_form_test_user', password='')
        another_user = User.objects.create_user(username='another_feedback_form_test_user', password='')

        profile = Profile.objects.get(pk=another_user.pk)
        self.client.login(username='feedback_form_test_user', password='')
        response = self.client.get(reverse('users:update', kwargs={'pk': profile.pk}))
        self.assertEqual(response.status_code, 403)
