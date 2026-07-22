from ninja import ModelSchema

from blog_app.models import Post, Category


class PostInSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ('title', 'content', 'published', 'category')


class PostOutSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'content', 'category', 'author', 'published', 'created_at')


class CategoryInSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ('title', 'slug')

class CategoryOutSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')
