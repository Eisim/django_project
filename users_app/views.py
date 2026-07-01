from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from users_app.forms import ProfileForm
from users_app.mixins import AuthorRequiredMixin
from users_app.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        profile, _ = Profile.objects.get_or_create(user__id=pk)
        return profile


class ProfileUpdateView(AuthorRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_update.html'

    def get_success_url(self):
        return reverse_lazy('users:details', kwargs={'pk': self.object.user.id})

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        profile = get_object_or_404(Profile, user__id=pk)
        return profile



class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:index')
