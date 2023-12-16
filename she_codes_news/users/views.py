from typing import Any
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views import generic

from .models import CustomUser
from news.models import NewsStory

from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect

from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm


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
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context
    
    def ChangePasswordDoneView(request):
        return render(request, 'users/changePassword_done.html', {})
    
    def ChangePasswordView(request):
        if request.method == 'POST':
            form = auth_views.PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('users:changePassword_done')
        else:
            form = auth_views.PasswordChangeForm(request.user)
        return render(request, 'users/changePassword.html', {'form': form})


# Which type of Django generic when?
    # generic.ListView for seeing all (or a subset) of a data model
    # generic.DetailView for seeing one specific item from a model
# Now the edit versions:
    # generic.edit.CreateView for creating a new item in a model
    # generic.edit.UpdateView for modifying one specific item from a model
    # generic.edit.DeleteView for removing one specific item from a model

