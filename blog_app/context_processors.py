from django.contrib.auth.models import User

from blog_app.models import Category, Post


def categories_processor(request):
    return {
        'nav_categories': Category.objects.all(),
    }

def blog_stats_processor(request):
    return {
        'total_posts': Post.objects.filter(published=True).count(),
        'total_users': User.objects.all().count(),
    }
