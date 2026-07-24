from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_app.api import PostViewSet, CategoryViewSet

app_name = 'drf_app'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]
