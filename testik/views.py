from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm
from .models import Post


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


def index(request):
    posts = Post.objects.all()
    if request.method == "POST":
        pass
    context = {'posts': posts}
    return render(request, 'index.html', context)
