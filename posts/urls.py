from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('group/<int:group_id>/', views.group_profile, name='group_profile'),
]
