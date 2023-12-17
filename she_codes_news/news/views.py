from typing import Any
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import NewsStory, StoryForm, CommentForm
from news.models import NewsStory
from users.models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import request
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm


# Index News Block
class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        '''Order all stories and latest stories in negative chronology
        Display latest stories from 0 to 3 index
        Return the latest 4 stories and all stories in reverse chronolgy'''
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = stories
        return context

# Exploring All Stories Block
class ExploreView(generic.ListView):
    model = CustomUser
    template_name = 'news/exploreStories.html'

    def get_queryset(self):
        '''Return all news stories'''
        return NewsStory.objects.all()

    def get_queryset(self):
        '''Return all authors for stories'''
        return CustomUser.objects.all()
    
    def get_context_data(self, **kwargs):
        '''Return all stories in reverse date + time order and list of users as story authors'''
        query = self.request.GET.get("author")
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['story_authors'] = CustomUser.objects.all()
        return context

# Story Block with Single Story View
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs): 
        '''Return a comment form and related comments'''
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["form_action"] = reverse_lazy("news:addComment", kwargs={"pk": self.kwargs.get('pk')})
        return context

# Add Story Block
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'StoryForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        '''Allocates author name as logged in user name
        Saves the form and redirects to the success URL'''
        form.instance.author = self.request.user
        return super().form_valid(form)

# Add a Comment Block
class AddCommentView(generic.CreateView):
    form_class = CommentForm
    success_url = reverse_lazy("news:newsStory")
    template_name = 'news/createComment.html'

    def form_valid(self, form):
        '''Saves the form and redirects to the success URL
        Allocates comment against logged in user ID and related story'''
        form.instance.author = self.request.user 
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        # alternative way / compacted code
        # form.instance.story = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        '''Returns to the story & shows new comment'''
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})
    # alternative way / compacted code 
        # return redirect("news:story", pk=self.kwargs.get("pk"))
    # def get_success_url(self):
    #     return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get("pk")})

# Edit Story Block
class EditStoryView(generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'story'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy("news:index")

    def form_valid(self, form):
        '''Saves the form & redirects to the success URL'''
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        '''Redirect top the edited story'''
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})

# Delete Story Block
class DeleteStoryView(TemplateView):
    model = NewsStory
    context_object_name = 'story'
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:deleteStory_done')

class DeleteStoryDoneView(TemplateView):
    '''Redirect to the deleted success page'''
    model = NewsStory
    template_name = '/news/deleteStory_done.html'
        # return render(request, 'news/deleteStory_done.html', {})


# # review the below before submission
# # Logged in Author Story List View
class AuthorStoryListView(generic.ListView):
    #  /author_1
    model = CustomUser
    template_name = 'news/index.html'
    context_object_name = 'latest_stories'

    def get_queryset(self):
        '''Return all news stories'''
        return NewsStory.objects.filter(author__username=self.kwargs['username'])

# Logged in Author Detail Story View
class AuthorDetailView(generic.DetailView):
    # /author_2
    model = CustomUser
    template_name = 'news/index.html'
    context_object_name = 'author'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

    def get_context_data(self, **kwargs): 
        '''Return all news stories'''
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.filter(author__id=self.object.id)
        return context
    
    # def redirect_view(request):
    #     response = redirect('/redirect-success/')
    #     return response