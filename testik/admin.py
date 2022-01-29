from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'text', 'author', 'group', 'date']
    search_fields = ['name', ]
    empty_value_display = '-Нема-'


class CommunityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'header', 'description', 'rules']
    search_fields = ['name', ]
    empty_value_display = '-Нема-'


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Community, CommunityAdmin)
