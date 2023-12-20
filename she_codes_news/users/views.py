from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views.generic.base import TemplateView

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class MyProfileView(TemplateView):
    model = CustomUser
    success_url = reverse_lazy
    template_name = 'users/profileView.html'

    def get_object(self, *args, **kwargs):
        return self.request.user