# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment

# Story Block
class StoryForm(ModelForm):
    class Meta: 
        model = NewsStory
        fields = ['pub_date', 'title', 'image_field', 'content', 'author']
        labels = {
            'title': ('Story Title'),
            'pub_date': ('Date Published'),
            'image_field': ('Image URL'),
            'content': ('Write a Story'),
            'author': ('Written By')
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-controls'}),
            'pub_date': forms.DateTimeInput(format=('%d/%m/%Y %H:%M'), attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'datetime-local', 
                    }),
            'image_field':forms.URLInput(attrs={'class':'form-control'},),
        }

# Comment Block
class CommentForm(ModelForm):
    class Meta: 
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment here'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ""



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

        # 'pub_date': forms.DateTimeInput(format=('%d/%m/%Y %H:%M'), attrs={
        #         'class':'form-control',
        #         'placeholder':'Select a date',
        #         'type':'datetime-local'}),
        # # 'author': what attributes am i adding in?