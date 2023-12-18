# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory

# Story Block
class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title', 'image', 'content']
        labels = {
            'title': ('Story Title'),
            'image': ('Image URL'),
            'content': ('Write a Story'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-controls'}),
            'image':forms.URLInput(attrs={'class':'form-control'}),
        }

# Comment Block
# class CommentForm(ModelForm):
#     class Meta: 
#         model = Comment
#         fields = ['content']
#         widgets = {
#             'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment here'})
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['content'].label = ""