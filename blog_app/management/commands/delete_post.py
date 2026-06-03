from django.core.management import BaseCommand

from blog_app.models import Post


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--post_id', type=int, required=True)

    def handle(self, *args, **options):
        post_id = options['post_id']
        post: Post | None = None
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            self.stdout.write(self.style.WARNING("Post not found"))
        except Exception:
            self.stdout.write(self.style.ERROR("Unexpected error"))
        if not post:
            return

        post.delete()
        self.stdout.write(self.style.SUCCESS(f"Post deleted: {post_id}"))
