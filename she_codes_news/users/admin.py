# Setting up Users Step 4: tie the new model & forms to the admin view

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)

# CustomUser & CustomeUserAdmin = custom admin interface for CustomUser model using the CustomUserAdmin  class
# add_form and form attributes to custome create and change forms (allows for customising the user creation and editing processes in Django admin)
#  admin.site.register(CustomUser, CustomUserAdmin) associates the custom admin configuration with the CustomUser model in Django admin