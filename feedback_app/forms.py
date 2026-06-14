from django import forms


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
