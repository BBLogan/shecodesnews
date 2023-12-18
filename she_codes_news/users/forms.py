# users/forms.py
# Setting up Users Step 3: create forms for a user login and updating

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class PasswordChangeForm(PasswordResetForm):
    class Meta:
        model= CustomUser
        fields = ['username', 'email', 'password']

# If needed could add 'first_name', 'last_name' to the fields of CustomUser model and would ned to include it in both the CustomUserCreationForm and CustomUserChangeForm fields list e.g., fields = ['username', 'email', 'first_name', 'last_name'] 