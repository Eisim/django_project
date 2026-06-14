from django.shortcuts import render, redirect

from feedback_app.forms import FeedbackForm
from feedback_app.models import Feedback


def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            Feedback.objects.create(name=name, email=email, message=message)
            return redirect('blog:index')
    else:
        form = FeedbackForm()

    context = {'form': form}
    return render(request, 'feedback_page.html', context)
