from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

# django.db.models.BigAutoField setting is used to define the type of primary key Django should use when creating models
