# users/urls.py
# from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CreateAccountView, AccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', AccountView.as_view(), name='profile'),
]


# pk = primary key - links the relationship between two models or databases
# ID pk for identifying individual users
# User = logged in 
# Vistor = not logged in