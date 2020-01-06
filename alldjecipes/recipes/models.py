'''
Creator (of recipe)

'''

from django.db import models
from alldjecipes.users.models import ChefUser
from django.utils import timezone


class Recipe(models.Model):
    creator = models.ForeignKey(ChefUser, on_delete=models.DO_NOTHING,)
    recipe_name = models.CharField(max_length=50)
    completion_time = models.CharField(max_length=50)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    difficulty_level = models.BooleanField(default=True)
    APPETIZER = 'Appetizer'
    BREAKFAST = 'Breakfast'
    BRUNCH = 'Brunch'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    MEAL_CATEGORY = [
        (APPETIZER, 'Appetizer'),
        (BREAKFAST, 'Breakfast'),
        (BRUNCH, 'Brunch'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner')
    ]
    category = models.CharField(
        max_length=9,
        choices=MEAL_CATEGORY,
        null=False,
    )
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default='alldjecipes/images/defaultimage.jpeg')
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    contact = models.EmailField(ChefUser, max_length=254,default='')
    
    def __str__(self):
        return f"{self.recipe_name}"

class Comment(models.Model):
    recipebase = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING, null=False)
    commentor = models.ForeignKey(ChefUser, on_delete=models.DO_NOTHING)
    content = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.content} by {self.commentator}'