from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/create/', views.post_create, name='post_create'),

    path('posts/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
]
app_name = 'blog'
