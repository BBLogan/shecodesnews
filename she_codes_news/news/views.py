from typing import Any
from users.models import CustomUser

from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.forms import CommentForm

from .models import NewsStory
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        return 

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AuthorStoryListView(generic.ListView):
    #  /author_1
    model = CustomUser
    template_name = 'news/index.html'
    context_object_name = 'latest_stories'

    def get_queryset(self):
        '''Return all news stories'''
        return NewsStory.objects.filter(author__username=self.kwargs['username'])

class AuthorDetailView(generic.DetailView):
    # /author_2
    model = CustomUser
    template_name = 'news/index.html'
    context_object_name = 'author'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.filter(author__id=self.object.id)
        return context

class AddCommentView(generic.CreateView):
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        pk = self.kwargs.get("pk")
        form.instance.story = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get("pk")})

    
    # def redirect_view(request):
    #     response = redirect('/redirect-success/')
    #     return response