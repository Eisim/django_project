from .models import Post, Category
from django.shortcuts import get_object_or_404, render


def index(request):
    posts = Post.objects.filter(published=True)
    context = {
        'posts': posts[:5]
    }
    return render(request, 'index.html', context)


def __http_post_response(post: Post) -> str:
    return f'<li>{post.created_at}) <a href=\"/posts/{post.slug}/\">{post.title}</a> | {post.author}</li>'


def __http_category_response(category: Category) -> str:
    return f'<li><a href="/categories/{category.id}">{category.title}</a></li>'


def posts_list(request):
    posts = Post.objects.filter(published=True)

    context = {
        'posts': posts,
    }

    return render(request, 'posts_list.html', context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    post.increase_views_count()
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)


def categories_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories_list.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published=True)

    context = {
        'category': category,
        'posts': posts,
    }

    return render(request, 'category_detail.html', context)
