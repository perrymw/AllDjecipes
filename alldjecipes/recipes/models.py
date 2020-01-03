'''
Creator (of recipe)

'''

from django.db import models
from alldjecipes.users.models import ChefUser, Creator
from django.utils import timezone


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
    

