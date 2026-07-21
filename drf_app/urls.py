from django.urls import path

from drf_app import api

app_name='drf_app'


urlpatterns = [
    path('posts/', api.PostListCreateAPIView.as_view(),name='post-list-create'),
    path('posts/<int:pk>', api.PostRetrieveUpdateDestroyAPIView.as_view(),name='post-detail'),

    path('categories/', api.CategoryListCreateAPIView.as_view(),name='category-list-create'),
    path('categories/<int:pk>', api.CategoryRetrieveUpdateDestroyAPIView.as_view(),name='category-detail'),
]
