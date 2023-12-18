# users/urls.py
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CreateAccountView, AccountView, ChangePasswordView, ChangePasswordDoneView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', AccountView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='changePassword'),
    path('change-password-done/', ChangePasswordDoneView.as_view(), name='changePassword_done'),
]

# pk = primary key - links the relationship between two models or databases
# ID pk for identifying individual users
# User = logged in 
# Vistor = not logged in