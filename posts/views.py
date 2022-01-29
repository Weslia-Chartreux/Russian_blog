from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from testik.models import User, Post

from testik.models import Community


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    count_posts = len(list(Post.objects.filter(author=profile_user)))
    all_posts = Post.objects.filter(author=profile_user)
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'profile_user': profile_user,
        'count_posts': count_posts,
        'posts': page_obj,
    }
    return render(request, 'profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    count_posts = len(list(Post.objects.filter(author=post.author)))
    context = {
        'post': post,
        'count_posts': count_posts,
    }
    return render(request, 'post_detail.html', context)


def group_profile(request, group_id):
    group = get_object_or_404(Community, id=group_id)
    count_posts = len(list(Post.objects.filter(group=group)))
    all_posts = Post.objects.filter(group=group)
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'profile_user': group,
        'count_posts': count_posts,
        'posts': page_obj,
    }
    return render(request, 'group_profile.html', context)
