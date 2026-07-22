from ninja import ModelSchema

from blog_app.models import Post


class PostInSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ('title', 'content', 'published', 'category')


class PostOutSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'content', 'category', 'author', 'published', 'created_at')
