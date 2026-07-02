from django import forms
from slugify import slugify

from blog_app.models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']  # 'author', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержимое статьи'}),
            # 'author': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }

        labels = {
            'title': 'Заголовок статьи',
            'content': 'Содержание статьи',
            # 'author': 'Автор',
            'category': 'Категория',
            'image': 'Обложка поста'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Заголовок должен быть длиннее 5 символов")

        return title
    def save(self, *args, **kwargs):
        instance = super().save(commit=False)
        instance.published = True
        instance.save()
        return instance


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100,
                            label="Поиск по статьям",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Введите текст для поиска'}),
                            )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        categories = Category.objects.filter(slug=slugify(title))

        if categories.exists():
            raise forms.ValidationError("Такая категория уже существует")
        return title
