from django.views.generic import DetailView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from users_app.models import Profile
from users_app.forms import ProfileForm
from users_app.mixins import AuthorRequiredMixin

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        profile = get_object_or_404(Profile, user__id=pk)
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
