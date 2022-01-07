from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
