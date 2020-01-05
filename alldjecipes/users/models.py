from django.db import models
from django.contrib.auth.models import AbstractUser

class ChefUser(AbstractUser):
    pass

# class Creator(models.Model):
#     user = models.OneToOneField(ChefUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
#     def __str__(self):
#         return f"{self.name}"
