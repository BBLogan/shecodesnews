from django.contrib import admin
from .models import NewsStory, Comment

# Register your models here

# News Story Block
class NewsStoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Story Data', {'fields': ['title']}),
        (None, {'fields': ['author']}),
        (None, {'fields': ['pub_date']}),
        ('Story Content', {'fields': ['image_field']}),
        (None, {'fileds': ['content']}),
    ]
    list_display = ('title', 'author', 'pub_date')

admin.site.register(NewsStory, NewsStoryAdmin)

# Admin Block
class CommentAdmin(admin.ModelAdmin):
    list_display = ('story', 'author', 'content', 'created_at', 'modified_at')
    list_filter = ('created_at', 'story')
    search_fields = ('author', 'content', 'story')

admin.site.register(Comment, CommentAdmin)