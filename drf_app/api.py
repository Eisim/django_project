from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAdminUser
from slugify import slugify

from blog_app.models import Post, Category
from drf_app.serializers import PostSerializer, CategorySerializer
from drf_app.permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ['category', 'published']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        slug = slugify(title)
        serializer.save(author=self.request.user, slug=slug)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['title']
    ordering_fields = ['title', ]

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            return [IsAdminUser()]
        else:  # elif self.action in ['list', 'retrieve']:
            return [AllowAny()]
