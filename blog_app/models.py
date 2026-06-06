from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"
        ordering: list[str] = ["id"]

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок статьи")
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name="Текст статьи")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    published = models.BooleanField(default=False, verbose_name="Статус публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    views_count = models.IntegerField(default=0, verbose_name="Число просмотров")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', default=1,
                                 verbose_name="Категория")

    class Meta:
        verbose_name: str = "Статья"
        verbose_name_plural: str = "Статьи"
        ordering: list[str] = ["created_at"]

    def __str__(self):
        return self.title

    def increase_views_count(self):
        self.views_count += 1
        self.save()
