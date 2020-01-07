from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import View
from alldjecipes.recipes.forms import CommentForm, RecipeForm
from alldjecipes.recipes.models import Recipe, Comment


def index(request):
    html = "index.html"
    
    recipe = Recipe.objects.all()

    return render(request, html, {"data": recipe})


def recipe_detail(request, id):
    html = 'recipeview.html'
    recipe = Recipe.object.filter(id=id).first()
    comments = Comment.object.all()
    ingredients, instructions = recipe.ingredients, recipe.instructions
    if '.' in ingredients or instructions:
        ingredients, instructions = recipe.ingredients.split('.'), recipe.instructions.split('.')

    return render(request, html, {"ingredients": ingredients, "instructions": instructions, "recipe": recipe})


class AddRecipe(View):
    html = 'generic_form.html'
    def get(self, request):
        form = RecipeForm()
        return render(request, self.html, {'form': form})
    def post(self, request):
        if request.method == 'POST':
            form = RecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_recipe = Recipe.objects.create(
                    recipe_name=data['recipe_name'],
                    difficulty_level=data['difficulty_level'],
                    category=data['category'],
                    ingredients=data['ingredients'],
                    instructions=data['instructions'],
                    completion_time=data['completion_time'],
                    image=data['image']
                    )
            return HttpResponseRedirect(reverse('homepage'))
        form = RecipeForm()
        return render(request, html, {'form': form})