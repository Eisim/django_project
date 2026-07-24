from django.contrib.auth.models import User
from django.test import TestCase

from blog_app.models import Post, Category


class PostModelTest(TestCase):
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

    def test_post_fields_creation(self):
        self.assertEqual(self.post.title, 'Тестовый пост')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.content, 'Содержимое для проверки автотестов.')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.category, self.category)
        self.assertTrue(self.post.published, self.user)

    def test_post_published_default_value(self):
        draft_post = Post.objects.create(
            title='Пост конца фантазии',
            slug='post-kontsa-fantasii',
            content='Не ну придумывать для теста что-то такое себе',
            category=self.category,
            author=self.user,
        )
        self.assertFalse(draft_post.published)
