from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from slugify import slugify

from blog_app.models import Post


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--title', type=str, required=True)
        parser.add_argument('--author', type=str, required=True)
        parser.add_argument('--content', type=str, required=True)


    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options['author'])
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING("User not found"))
            return

        slug = slugify(options['title'])
        post = Post.objects.create(author=user,
                                   content=options['content'],
                                   title=options['title'],
                                   slug=slug)
        self.stdout.write(self.style.SUCCESS(f"Post created: {post.id}"))
