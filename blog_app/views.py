from .forms import PostForm, SearchForm, CategoryForm
from .models import Post, Category
from django.shortcuts import get_object_or_404, render, redirect

from slugify import slugify


def index(request):
    search_form = SearchForm(data=request.GET)
    posts = Post.objects.filter(published=True)

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(title__icontains=query)

    context = {
        'posts': posts[:5],
        'search_form': search_form,
    }
    return render(request, 'index.html', context)


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
        'post': post,
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


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect(r'blog:post_detail', post_slug=post.slug)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'post_create.html', context)


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.title)
            category.save()
            return redirect(r'blog:category_detail', category_id=category.id)
    else:
        form = CategoryForm()

    context = {
        'form': form,
    }
    return render(request, 'category_create.html', context)


def post_edit(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(r'blog:post_detail', post_slug=post.slug)
    context = {
        'form':form,
    }
    return render(request, 'post_edit.html', context=context)
