from .forms import PostForm, CategoryForm
from .models import Post, Category
from django.shortcuts import get_object_or_404, render, redirect

from slugify import slugify

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.filter(published=True)
        return queryset.order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class PostFormBase:
    model = Post
    form_class = PostForm


class PostCreateView(PostFormBase, CreateView):
    template_name = 'post_create.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostUpdateView(PostFormBase, UpdateView):
    template_name = 'post_edit.html'
    success_url = reverse_lazy('blog:index')
    slug_url_kwarg = 'post_slug'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('blog:index')
    slug_url_kwarg = 'post_slug'


def posts_list(request):
    posts = Post.objects.filter(published=True)

    context = {
        'posts': posts,
    }

    return render(request, 'posts_list.html', context)


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
