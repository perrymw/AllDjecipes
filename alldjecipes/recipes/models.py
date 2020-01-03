'''
Creator (of recipe)

'''

from django.db import models
from alldjecipes.users.models import User
from django.utils import timezone

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.name}"

class Recipe(models.Model):
    recipe_name = models.TextField(blank=False)
    completion_time = models.CharField(max_length=50)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    difficulty_level = models.BooleanField(default=True)
    APPETIZER = 'Appetizer'
    BREAKFAST = 'Breakfast'
    BRUNCH = 'Brunch'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    mealcategory = [
        (APPETIZER, 'Appetizer'),
        (BREAKFAST, 'Breakfast'),
        (BRUNCH, 'Brunch'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner')
    ]
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default='alldjecipes/images/defaultimage.jpeg')
