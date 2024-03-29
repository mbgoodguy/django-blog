from django.contrib import admin

from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'author',
        'status',
        'publish',
        'updated'
    ]
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish', 'updated']
    list_editable = ('status',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created', 'updated', 'active', 'post']
    list_filter = ['created', 'updated', 'active', 'post']
    search_fields = ['name', 'email', 'body', 'post__title', 'post__body']
