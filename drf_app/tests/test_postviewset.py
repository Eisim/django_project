from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from blog_app.models import Post, Category


class TestPostViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.admin_user = User.objects.create_superuser(username='admin', email='', password='admin_password')
        self.base_user = User.objects.create_user(username='base', email='', password='base_password')

        self.category = Category.objects.create(title='category')
        self.post = Post.objects.create(
            title='Post Title',
            slug='post-titile',
            content='Post Content',
            author=self.base_user,
            category=self.category,
            published=True
        )

    def test_get_posts(self):
        response = self.client.get(reverse('drf:post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_by_anonymous(self):
        data = {
            'title': 'Anon Post Title',
            'content': 'Anon Post Content',
            'category': self.category.pk,
        }
        self.client.force_authenticate(None)
        response = self.client.post(reverse('drf:post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_by_authenticated(self):
        data = {
            'title': 'Anon Post Title',
            'content': 'Anon Post Content',
            'category': self.category.pk,
        }
        self.client.force_authenticate(self.base_user)
        response = self.client.post(reverse('drf:post-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
