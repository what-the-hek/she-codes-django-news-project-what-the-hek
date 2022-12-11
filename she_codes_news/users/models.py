from django.contrib.auth.models import AbstractUser

# this lets us get all the user stuff Django provides (username, password etc), but then we can also add to it
class CustomUser(AbstractUser):
    pass

    # this gives me the name of the user on screen
    def __str__(self):
        return self.username
