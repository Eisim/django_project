from django.db import IntegrityError
from django.test import TestCase

from django.contrib.auth.models import User

from blog_app.models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cat_test_user', password='securepassword123')
        self.category = Category.objects.create(
            title='Base category object',
            slug='base-category-object',
        )

    def test_category_correct_fields(self):
        self.assertEqual(self.category.title, 'Base category object')
        self.assertEqual(self.category.slug, 'base-category-object')

    def test_str_dunder_method(self):
        self.assertEqual(self.category.__str__(), 'Base category object')

    def test_unique_slug_field(self):
        with self.assertRaises(IntegrityError):
            Category.objects.create(
                title='Another category object',
                slug='another-category-object',
            )
            Category.objects.create(
                title='Another category object',
                slug='another-category-object',
            )
