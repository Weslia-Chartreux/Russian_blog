from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'text', 'author', 'date']
    search_fields = ['name', ]
    empty_value_display = '-Нема-'


admin.site.register(models.Post, PostAdmin)
