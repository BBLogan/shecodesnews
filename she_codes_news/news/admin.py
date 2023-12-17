from django.contrib import admin
from .models import NewsStory, Comment

# News Story Block
class NewsStoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Story Data', {'fields': ['title', 'author', 'pub_date']}),
        ('Story Content', {'fields': ['image_field', 'content']}),
    ]
    list_display = ('title', 'author', 'pub_date')

admin.site.register(NewsStory, NewsStoryAdmin)

# Admin Block
class CommentAdmin(admin.ModelAdmin):
    list_display = ('story', 'author', 'content', 'created_at', 'modified_at')
    list_filter = ('created_at', 'story')
    search_fields = ('author__username', 'content', 'story__title')

admin.site.register(Comment, CommentAdmin)