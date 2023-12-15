from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

#  Newstory Block
class NewsStory(models.Model):
    '''Required data for story creation, editing and deleting
    Connected to user_model to allocate stories to logged in users
    Returns - Story Titel with __str__ override'''
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_field = models.URLField(null=True, blank=True)

    # display stroy title in admin portal on list
    def __str__(self):
        return self.title

# Comment Block
class Comment(models.Model):
    '''Data required for users to comment on stories
    Returns - Comment Content with __str__ override'''
    story = models.ForeignKey(NewsStory, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(USER, on_delete=models.CASCADE, null=True,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content