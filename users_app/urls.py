from django.urls import path

from users_app.views import ProfileUpdateView, ProfileDetailView

app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>/update', ProfileUpdateView.as_view(), name='update'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='details'),
]
