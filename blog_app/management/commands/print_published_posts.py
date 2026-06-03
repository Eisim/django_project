from django.core.management import BaseCommand

from blog_app.models import Post


class Command(BaseCommand):


    def handle(self, *args, **options):
        posts = Post.objects.filter(published=True)
        if not posts.exists():
            self.stdout.write(self.style.WARNING("No published posts found"))
            return

        for post in posts:
            self.stdout.write(f"{post.id}: {post.title} - {post.created_at:%Y-%m-%d}")
        self.stdout.write(self.style.SUCCESS(f"Найдено опубликованных постов: {posts.count()}"))
