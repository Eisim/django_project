from rest_framework import serializers
from blog_app.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'category', 'author', 'published', 'created_at']
        read_only_fields = ['created_at', 'slug', 'author']

class CategorySerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['title', 'slug', 'id', 'posts_count']

    def get_posts_count(self, obj) -> int:
        post_count = Post.objects.filter(category=obj.id, published=True).count()
        return post_count
