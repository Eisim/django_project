from django import forms

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
