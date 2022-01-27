from django.contrib import admin
from .models import Blog, Comment
from tinymce.models import HTMLField

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Blog.
    Which fields to include in the:
    list/search views, how they are filtered,
    which are prepopulated and
    creates an action to include approve Blogs.
    """
    fields = [
        'title',
        'slug',
        'author',
        'featured_image',
        'image_thumb',
        'alt_tag',
        'excerpt',
        'content',
        'status',
        'likes',
    ]

    list_display = (
        'image_thumb',
        'title',
        'slug',
        'status',
        'created_at',
        )

    search_fields = ['title', 'content', 'alt_tag',]
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish_Blog',]
    readonly_fields = ['image_thumb',]

    def publish_Blog(self, request, queryset):
        queryset.update(status=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Establish the view in admin for the Comments.
    Which fields to include in the:
    list/search views, how they are filtered and
    creates an action to include approve Blogs.
    """
    list_display = (
        'name',
        'body',
        'blog',
        'created_at',
        'approved'
        )
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments',]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
