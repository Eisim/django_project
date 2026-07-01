from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'social_link']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'social_link': forms.EmailInput(attrs={
                'class': 'form-control'}),
        }
        labels = {
            'bio': 'О Вас',
            'social_link': 'Контакт для связи'
        }


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control',
                 'placeholder': field.label}
            )


class CustomRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control',
                 'placeholder': field.label}
            )
