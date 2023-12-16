# users/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateAccountView, AccountView, ChangePasswordView, ChangePasswordDoneView


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    
    path('<int:pk>', AccountView.as_view(), name='profile'),

    path('change-password/', ChangePasswordView, name='changePassword'),

    path('change-password-done/', ChangePasswordDoneView, name='changePassword_done')
]

# pk = primary key - links the relationship between two models or databases
# ID pk for identifying individual users
# User = logged in 
# Vistor = not logged in 