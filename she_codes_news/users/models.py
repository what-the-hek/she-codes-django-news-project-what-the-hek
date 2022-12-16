from django.contrib.auth.models import AbstractUser
from django.db import models

# this lets us get all the user stuff Django provides (username, password etc), but then we can also add to it
class CustomUser(AbstractUser):
    profile_image = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    pass

    # this gives me the name of the user on screen
    def __str__(self):
        return self.username
