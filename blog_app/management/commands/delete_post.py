from django.core.management import BaseCommand

from blog_app.models import Post


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--post_id', type=int)

    def handle(self, *args, **options):
        post_id = options['post_id']
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            self.stdout.write(self.style.WARNING("Post not found"))
        post.delete()
        self.stdout.write(self.style.SUCCESS(f"Post deleted: {post_id}"))
