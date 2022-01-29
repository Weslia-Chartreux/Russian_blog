from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm
from .models import Post


class SignUp(CreateView):
    form_class = CreationForm
    success_url = '/'
    template_name = 'users/signup.html'


def index(request):
    posts = Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        pass
    context = {'posts': page_obj}
    return render(request, 'index.html', context)
