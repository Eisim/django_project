from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog_app.models import Post, Category


class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='securepassword123'
        )
        self.category = Category.objects.create(
            title='Категория для теста',
            slug='categoria-dlya-testa'
        )
        self.post = Post.objects.create(
            title='Тестовый пост',
            slug='test-post',
            content='Содержимое для проверки автотестов.',
            category=self.category,
            author=self.user,
            published=True
        )

    def test_homepage_status_response(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_correct_template(self):
        response = self.client.get(reverse('blog:index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_homepage_shows_published_post(self):
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, self.post.title)

    def test_homepage_hides_draft_posts(self):
        Post.objects.create(
            title='Тестовый пост-draft',
            slug='test-post-draft',
            content='Содержимое для проверки автотестов.',
            category=self.category,
            author=self.user,
            published=False
        )
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, 'Тестовый пост')
        self.assertNotContains(response, 'Тестовый пост-draft')

    def test_post_detail_page_status_code(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'post_slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_page_context(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'post_slug': self.post.slug}))
        self.assertEqual(response.context['post'], self.post)

    def test_post_detail_returns_404(self):
        response = self.client.get(reverse('blog:post_detail', kwargs={'post_slug': 'non-existent-slug'}))
        self.assertEqual(response.status_code, 404)
