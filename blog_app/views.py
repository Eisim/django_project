from django.http import HttpResponse
from .models import Post, Category
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse("<h1>Hello blog!</h1>")


def __http_post_response(post:Post) -> str:
    return f'<li>{post.created_at}) <a href=\"/posts/{post.id}/\">{post.title}</a> | {post.author}</li>'


def __http_category_response(category: Category) -> str:
    return f'<li><a href="/categories/{category.id}">{category.title}</a></li>'

def posts_list(request):

    posts = Post.objects.filter(published=True)
    response_header = "<h1>Published posts</h1>"
    post_list = f"<ul>{''.join([__http_post_response(post) for post in posts])}</ul>"
    http_response = f"{response_header}\n{post_list}"

    return HttpResponse(http_response)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    response_header = f"<h1>{post.title}</h1>"
    post_author = f"by: {post.author}"
    post_content = f"{post.content}"
    http_response = f"{response_header}\n{post_content}<br>{post_author}"
    return HttpResponse(http_response)
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
