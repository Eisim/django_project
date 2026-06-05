from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
]
