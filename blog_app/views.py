from django.http import HttpResponse
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
    response_header = "<h1>Published posts</h1>"
    post_list = f"<ul>{''.join([__http_post_response(post) for post in posts])}</ul>"
    http_response = f"{response_header}\n{post_list}"

    return HttpResponse(http_response)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)


def categories_list(request):
    categories = Category.objects.all()
    response_header = "<h1>Categories</h1>"
    category_list = f"<ul>{''.join([__http_category_response(category) for category in categories])}</ul>"
    http_response = f"{response_header}\n{category_list}"
    return HttpResponse(http_response)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    response_header = f"<h1>{category.title}</h1>"
    posts = Post.objects.filter(category=category, published=True)

    post_list = f"<ul>{''.join([__http_post_response(post) for post in posts])}</ul>"

    http_response = f"{response_header}\n{post_list}"
    return HttpResponse(http_response)
