from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post


# Функция, которая отвечает за показ домашней страницы
def index(request):
    posts = Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        pass
    context = {'posts': page_obj}
    return render(request, 'index.html', context)
