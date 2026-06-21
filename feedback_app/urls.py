from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback_page'),
    path('success/', views.feedback_success, name='success'),
]

app_name = 'feedback'
