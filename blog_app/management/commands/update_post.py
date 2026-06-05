from django.core.management import BaseCommand

from blog_app.models import Post


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--post_id', type=int, required=True)
        parser.add_argument('--title', type=str, required=True)

    def handle(self, *args, **options):
        post_id = options['post_id']
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            self.stdout.write(self.style.WARNING("Post not found"))
            return
        post.title = options['title']
        post.save()
        self.stdout.write(self.style.SUCCESS(f"Post updated: {post_id}. New title: {post.title}"))
