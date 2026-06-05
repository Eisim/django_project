from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse("<h1>Hello blog!</h1>")


def posts_list(request):
    def http_post_response(post:Post) -> str:
        return f'<li>{post.created_at}) <a href=\"/posts/{post.id}/\">{post.title}</a> | {post.author}</li>'

    posts = Post.objects.filter(published=True)
    response_header = "<h1>Published posts</h1>"
    posts_list = f"<ul>{''.join([http_post_response(post) for post in posts])}</ul>"
    http_response = f"{response_header}\n{posts_list}"

    return HttpResponse(http_response)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    response_header = f"<h1>{post.title}</h1>"
    post_author = f"by: {post.author}"
    post_content = f"{post.content}"
    http_response = f"{response_header}\n{post_content}<br>{post_author}"
    return HttpResponse(http_response)
