from django.contrib import admin
from django.contrib.admin import register as admin_register
from .models import Post, Comment, Like


# Register your models here.
@admin_register
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'image', 'liked']



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

