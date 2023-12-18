from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from users.forms import CustomUserCreationForm
from news.models import NewsStory, Comment
# from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class AccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.request.user).order_by('-pub_date')
        context['user_comments'] = Comment.objects.filter(author=self.request.user).order_by('-date')
        return context

# In Django generics, use:
# - generic.ListView for displaying a list of items (e.g., a list of news stories)
# - generic.DetailView for showing details of a specific item (e.g., a detailed view of a user profile)
# - generic.edit.CreateView for creating a new item (e.g., user account registration)
# - generic.edit.UpdateView for modifying an existing item (e.g., updating user profile information)
# - generic.edit.DeleteView for removing an item (e.g., deleting a user account)
