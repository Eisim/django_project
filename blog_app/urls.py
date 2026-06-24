from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('posts/', views.PostListPageView.as_view(), name='posts_list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<slug:post_slug>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<slug:post_slug>/delete', views.PostDeleteView.as_view(), name='post_delete'),

    path('posts/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
]
app_name = 'blog'
