from django import forms

SUBJECT_CHOICES = [
        ('tech', 'Технический вопрос'),
        ('collaboration', 'Сотрудничество'),
        ('complaint', 'Жалоба'),
        ('other', 'Другое'),
    ]

class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Ваше имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите свое имя'
            }
        )
    )
    email = forms.EmailField(
        label='Ваш email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите свой email'
        })
    )
    message = forms.CharField(
        label='Ваше обращение',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Ваше обращение',
            'rows': 5
        })
    )
    subject = forms.ChoiceField(
        label='Тема обращения',
        choices=SUBJECT_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'выберите тему обращения'
            }
        )
    )
