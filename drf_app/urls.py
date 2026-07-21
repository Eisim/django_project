from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_app import api
from drf_app.api import PostViewSet

app_name='drf_app'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    # path('posts/', api.PostListCreateAPIView.as_view(),name='post-list-create'),
    # path('posts/<int:pk>', api.PostRetrieveUpdateDestroyAPIView.as_view(),name='post-detail'),
    path('', include(router.urls)),
    path('categories/', api.CategoryListCreateAPIView.as_view(),name='category-list-create'),
    path('categories/<int:pk>', api.CategoryRetrieveUpdateDestroyAPIView.as_view(),name='category-detail'),


]
