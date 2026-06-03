from dataclasses import dataclass, asdict

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from slugify import slugify

from blog_app.models import Post


@dataclass(frozen=True)
class ArgInfo:
    type: type


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.used_args: dict[str, ArgInfo] = {
            '--title': ArgInfo(str),
            '--author': ArgInfo(str),
            '--content': ArgInfo(str),

            # '--category': ArgInfo(str),

            # '--published': ArgInfo(bool),
        }

    def add_arguments(self, parser):
        for arg_name, arg_info in self.used_args.items():
            parser.add_argument(arg_name, **asdict(arg_info))

    def get_user(self, username: str) -> User:
        user: User | None = None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING("User not found"))
        return user

    def handle(self, *args, **options):
        user = self.get_user(options['author'])
        slug = slugify(options['title'])
        self.stdout.write(f"{options['title']} - {slug}")
        post = Post.objects.create(author=user,
                                   content=options['content'],
                                   title=options['title'],
                                   slug=slug)
        post.save()
        self.stdout.write(self.style.SUCCESS(f"Post created: {post.id}"))
