from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



class ChefUser(AbstractUser):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username}'
    
