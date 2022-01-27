from django.shortcuts import render, get_object_or_404

from testik.models import User, Post


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    count_posts = len(list(Post.objects.filter(author=profile_user)))
    all_posts = Post.objects.filter(author=profile_user)
    context = {
        'profile_user': profile_user,
        'count_posts': count_posts,
        'all_posts': all_posts,
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
