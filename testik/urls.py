from django.urls import path, include
from .views import index
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='index'),


]