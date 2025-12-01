from django.contrib import admin
from .models import Author, BlogPost, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'posts_count']
    search_fields = ['name']
    list_display_links = ['name']
    ordering = ['name']
    
    # Custom method to show post count
    def posts_count(self, obj):
        return obj.posts.count()
    posts_count.short_description = 'Number of Posts'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at', 'comments_count']
    list_filter = ['status', 'created_at', 'author']
    search_fields = ['title', 'content', 'author__name']
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['title', 'content', 'author', 'status']
        }),
        ('Dates', {
            'fields': ['published_at', ('created_at', 'updated_at')],
            'classes': ['collapse']  
        }),
    ]
    
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    def comments_count(self, obj):
        return obj.comments.count()
    comments_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['truncated_content', 'author', 'post', 'parent', 'created_at', 'is_deleted']
    list_filter = ['is_deleted', 'created_at', 'post']
    search_fields = ['content', 'author__name', 'post__title']
    actions = ['mark_as_deleted', 'mark_as_active']
    
    fields = ['post', 'author', 'content', 'parent', 'is_deleted', 'created_at']
    readonly_fields = ['created_at']
    
    # Custom display method (shows first 50 chars)
    def truncated_content(self, obj):
        if len(obj.content) > 50:
            return f"{obj.content[:50]}..."
        return obj.content
    truncated_content.short_description = 'Content'
    
    # Custom admin actions
    def mark_as_deleted(self, request, queryset):
        updated = queryset.update(is_deleted=True)
        self.message_user(request, f'{updated} comments marked as deleted.')
    mark_as_deleted.short_description = "Mark selected comments as deleted"
    
    def mark_as_active(self, request, queryset):
        updated = queryset.update(is_deleted=False)
        self.message_user(request, f'{updated} comments marked as active.')
    mark_as_active.short_description = "Mark selected comments as active"


