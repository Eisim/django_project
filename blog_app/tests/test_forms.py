from django.contrib.auth.models import User
from django.test import TestCase

from blog_app.models import Category
from blog_app.forms import PostForm


class FormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='securepassword123'
        )
        self.category = Category.objects.create(
            title='Категория для теста',
            slug='categoria-dlya-testa'
        )

    def test_form_with_valid_data(self):
        form_data = {
            'title': 'Первый возрощенный в тесте',
            'slug': 'pervii-vozroshenii-v-teste',
            'content': 'Текст интересного поста.',
            'category': self.category.pk,
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_empty_title(self):
        form_data = {
            'slug': 'pervii-vozroshenii-v-teste-2',
            'content': 'Текст интересного поста.',
            'category': self.category.pk,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_with_empty_content(self):
        form_data = {
            'title': 'Первый возрощенный в тесте',
            'slug': 'pervii-vozroshenii-v-teste-3',
            'category': self.category.pk,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
