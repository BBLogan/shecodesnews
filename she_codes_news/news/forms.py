# Forms Set Up Step 1: creating a forms.py file
# Forms Set Up Step 2: adding a ModelForm class

# /news/form.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content']
        widgets = {'pub_date': forms.DateInput(format='%m/%d/%Y', attrs={'class': 'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
