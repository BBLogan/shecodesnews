# news/forms.pyfields
from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Comment

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import NewsStory

class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            )
        }

class CommentForm(ModelForm):
    class Meta: 
        model = Comment
        fields = ['title', 'author', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            )
        }

# class CommentForm(forms.Form):
#     name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     subject = forms.CharField(max_length=150)
#     message = forms.CharField(widget=forms.Textarea)

#     def send_message(name, message):
#         if request.method == 'POST':
#             send_message(
#                 form.cleaned_data['name'],
#                 form.cleaned_data['message']
#             )


#     def comment_view(request):
#         if request.method == 'POST': 
#             form = CommentForm(request.POST)
#             if form.is_valid(): 
#                 pass
#                 return redirect('/success/')
#         else:
#             form = CommentForm()
        
#         return render(request, 'forms.html', {'form': form})
    
#     def success(request):
#         return HttpResponse('Success!')