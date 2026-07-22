from ninja import Router
from ninja.errors import HttpError
from slugify import slugify

from blog_app.models import Post
from ninja_app.schemas import PostOutSchema, PostInSchema

from django.contrib.auth.models import User

router = Router()


@router.get("/ping")
async def ping(request):
    return {
        "pong": True,
    }


@router.get(path="/posts", response=list[PostOutSchema])
async def posts(request, search: str | None = None, category_id: int | None = None):

    query_set = Post.objects.filter(published=True)

    if search:
        query_set = query_set.filter(title__icontains=search)

    if category_id:
        query_set = query_set.filter(category__id=category_id)

    posts = [post async for post in query_set]
    return posts


@router.get(path="/posts/{post_id}", response=PostOutSchema)
async def get_post(request, post_id):
    try:
        post = await Post.objects.aget(id=post_id)
    except Post.DoesNotExist:
        raise HttpError(status_code=404, message="Статья не найдена")
    return post


@router.post(path="/posts", response={201: PostOutSchema})
async def create_post(request, payload: PostInSchema):
    post_data = payload.dict()
    post_data['slug'] = slugify(post_data['title'])
    post_data['category_id'] = post_data.pop('category')

    if request.user.is_authenticated:
        post_data['author'] = request.user
    else:
        post_data['author'] = await User.objects.afirst()

    new_post = await Post.objects.acreate(**post_data)
    return 201, new_post
