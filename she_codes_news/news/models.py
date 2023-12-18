# Vistor = individual browsing website but with no account &/ not logged in
# User = visitor with an account & who's logged into the site
from django.db import models
from django.contrib.auth import get_user_model

#  Newstory Block
class NewsStory(models.Model):
    """
    Required data for story creation, editing and deleting
    Returns the story title with __str__ override
    Connected to user_model to allocate stories to logged in users
    """
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200, 
        help_text="Enter the title of the news story")
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(null=True, blank=True)

    # display story title in admin portal in a list
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = "News Stories"

# Comment Block
class Comment(models.Model):
    """
    Data required for users to comment on stories
    Returns - Comment Content with __str__ override
    """
    story = models.ForeignKey(
        NewsStory, 
        related_name="comments", 
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        help_text="Author of the news story",
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.TextField(help_text="Enter your comment here")

    def __str__(self):
        return self.content
    
    class Meta: 
        verbose_name_plural = "Comments"

# <!-- Assignemnt Notes -->
# This page is part of the news setup and additional features. It satisfies the following:
# [ ] Part 1: 