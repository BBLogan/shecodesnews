
# users/urls.py

from django.urls import path
from .views import CreateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
]