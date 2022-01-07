from django.shortcuts import render
from testik.models import Post


def index(request):
    posts = Post.objects.all()
    if request.method == "POST":
        pass
    context = {'posts': posts}
    return render(request, 'index.html', context)
