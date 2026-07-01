from .forms import PostForm, CategoryForm
from .models import Post, Category
from django.shortcuts import get_object_or_404, render

from slugify import slugify

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog_app.mixins import TitleMixin, StuffRequiredMixin


class IndexView(TitleMixin, ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 5
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_posts'] = Post.objects.filter(published=True).select_related('category', 'author')[:5]
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = Post.objects.filter(published=True)
        return queryset.order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.select_related('category', 'author')

    def get_object(self, queryset=None):
        object: Post = super().get_object(queryset)
        object.increase_views_count()
        return object


class PostFormBase:
    model = Post
    form_class = PostForm


class PostCreateView(StuffRequiredMixin, TitleMixin, PostFormBase, CreateView):
    template_name = 'post_create.html'
    success_url = reverse_lazy('blog:index')
    title = 'Создание новой статьи'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(StuffRequiredMixin, TitleMixin, PostFormBase, UpdateView):
    template_name = 'post_edit.html'
    success_url = reverse_lazy('blog:index')
    slug_url_kwarg = 'post_slug'
    title = 'Редактирование статьи'


class PostDeleteView(StuffRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('blog:index')
    slug_url_kwarg = 'post_slug'


class PostListPageView(TitleMixin, ListView):
    model = Post
    template_name = 'posts_list.html'
    paginate_by = 5
    context_object_name = 'posts'
    title = 'Список статей'

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-created_at')


class CategoryListView(TitleMixin, ListView):
    model = Category
    template_name = 'categories_list.html'
    paginate_by = 5
    context_object_name = 'categories'
    title = 'Каталог категорий'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=self.object, published=True).order_by('-created_at')
        return context


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published=True)

    context = {
        'category': category,
        'posts': posts,
    }

    return render(request, 'category_detail.html', context)


class CategoryFormBase:
    model = Category
    form_class = CategoryForm


class CategoryCreateView(CategoryFormBase, TitleMixin, CreateView):
    template_name = 'category_create.html'
    success_url = reverse_lazy('blog:index')
    title = 'Создание категории'
