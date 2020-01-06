from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from alldjecipes.recipes.forms import CommentForm, RecipeForm
from alldjecipes.recipes.models import Recipe, Comment

def recipe_detail(request, id):
    html = 'recipeview.html'
    recipe = Recipe.object.filter(id=id).first()
    ingredients, instructions = recipe.ingredients, recipe.instructions
    if '.' in ingredients or instructions:
        ingredients, instructions = recipe.ingredients.split('.'), recipe.instructions.split('.')

    return render(request, html, {"ingredients": ingredients, "instructions": instructions, "recipe": recipe})