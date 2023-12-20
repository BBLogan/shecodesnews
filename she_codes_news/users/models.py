# Users Setup Step 3: create the user model

# users/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username