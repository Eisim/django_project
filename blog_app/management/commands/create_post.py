from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from slugify import slugify

from blog_app.models import Post


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--title', type=str, required=True)
        parser.add_argument('--author', type=str, required=True)
        parser.add_argument('--content', type=str, required=True)

    def get_user(self, username: str) -> User:
        user: User | None = None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING("User not found"))
        except Exception:
            self.stdout.write(self.style.ERROR("Unexpected error"))
        return user

    def handle(self, *args, **options):
        user = self.get_user(options['author'])
        if not user:
            return

        slug = slugify(options['title'])
        post = Post.objects.create(author=user,
                                   content=options['content'],
                                   title=options['title'],
                                   slug=slug)
        self.stdout.write(self.style.SUCCESS(f"Post created: {post.id}"))
