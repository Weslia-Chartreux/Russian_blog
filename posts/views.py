from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from testik.models import User, Post

from testik.models import Community

from .forms import NewPostForm


# Функция, которая отвечает за показ страницы 'profile/<str:username>/'
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    count_posts = len(list(profile_user.posts.all()))
    all_posts = profile_user.posts.all()
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'profile_user': profile_user,
        'count_posts': count_posts,
        'posts': page_obj,
    }
    return render(request, 'profile.html', context)


# Функция, которая отвечает за показ страницы 'posts/<int:post_id>/'
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    count_posts = len(list(post.author.posts.all()))
    context = {
        'post': post,
        'count_posts': count_posts,
    }
    return render(request, 'post_detail.html', context)


# Функция, которая отвечает за показ страницы 'group/<int:group_id>/'
def group_profile(request, group_id):
    group = get_object_or_404(Community, id=group_id)
    count_posts = len(list(group.posts.all()))
    all_posts = group.posts.all()
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'profile_user': group,
        'count_posts': count_posts,
        'posts': page_obj,
    }
    return render(request, 'group_profile.html', context)


# Функция, которая отвечает за показ страницы 'create_post/'
def create_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            new_post = Post()
            new_post.name = form.cleaned_data['name']
            new_post.text = form['text'].value()
            if form['group'].value() != 'False':
                new_post.group = get_object_or_404(Community, id=form['group'].value())
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'new_post.html', {'form': NewPostForm()})