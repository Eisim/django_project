from ninja import Router
from ninja.errors import HttpError
from slugify import slugify

from blog_app.models import Post, Category
from ninja_app.schemas import PostOutSchema, PostInSchema, CategoryOutSchema, CategoryInSchema

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


@router.get('/categories', response=list[CategoryOutSchema])
async def categories(request, search_title: str | None = None):
    query_set = Category.objects.all()
    if search_title:
        query_set = query_set.filter(title__icontains=search_title)

    categories = [category async for category in query_set]
    return categories


@router.get('/categories/{category_id}', response=CategoryOutSchema)
async def get_category(request, category_id: int):
    try:
        category = await Category.objects.aget(id=category_id)
    except Category.DoesNotExist:
        raise HttpError(404, "Категория не найдена")
    return category


@router.post('/categories', response={201: CategoryOutSchema})
async def create_category(request, payload: CategoryInSchema):
    category_data = payload.dict()
    new_category, created = await Category.objects.aget_or_create(**category_data)

    if not created:
        raise HttpError(409, "Такая категория уже существует")

    return 201, new_category


@router.delete('/categories/{category_id}', response={204: None})
async def delete_category(request, category_id: int):
    try:
        category = await Category.objects.aget(id=category_id)
    except Category.DoesNotExist:
        raise HttpError(404, "Категории не существует")
    await category.adelete()
    return 204, None


@router.put('/categories/{category_id}', response={204: None})
async def update_category(request, category_id: int, payload: CategoryInSchema):
    update_data = payload.dict()
    updated_count = await Category.objects.filter(id=category_id).aupdate(**update_data)
    if updated_count == 0:
        raise HttpError(404, "Категории не существует")
    return 204, None
