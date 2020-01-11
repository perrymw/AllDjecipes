from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from alldjecipes.recipes.forms import CommentForm, RecipeForm
from alldjecipes.recipes.models import Recipe, Comment
from alldjecipes.helpers import helper


def index(request):
    html = "index.html"
    
    recipe = Recipe.objects.all()

    return render(request, html, {"recipe": recipe})


def recipe_detail(request, id):
    html = 'recipeview.html'
    recipe = Recipe.objects.filter(id=id).first()
    comments = Comment.objects.filter(recipebase=recipe)
    ingredients, instructions = recipe.ingredients, recipe.instructions
    if '.' in ingredients or instructions:
        ingredients, instructions = recipe.ingredients.split('.'), recipe.instructions.split('.')

    return render(request, html, {"ingredients": ingredients, "instructions": instructions, "recipe": recipe, 'comments':comments})


@method_decorator(login_required, name='dispatch')
class AddRecipe(View):
    html = 'generic_form.html'
    def get(self, request):
        form = RecipeForm()
        return render(request, self.html, {'form': form})
    def post(self, request):
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                new_recipe = Recipe.objects.create(
                    creator=request.user,
                    recipe_name=data['recipe_name'],
                    difficulty_level=data['difficulty_level'],
                    category=data['category'],
                    ingredients=data['ingredients'],
                    instructions=data['instructions'],
                    completion_time=data['completion_time'],
                    image=data['image'],
                    contact=request.user.email
                    )
            return HttpResponseRedirect(reverse('homepage'))
        form = RecipeForm()
        return render(request, html, {'form': form})

@method_decorator(login_required, name='dispatch')
class AddComment(View):
    html = 'generic_form.html'
    def get(self, request,id):
        form = CommentForm()
        return render(request, self.html, {'form': form})
    def post(self, request, id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_recipe = Comment.objects.create(
                    recipebase=Recipe.objects.filter(id=id).first(),
                    commentor=request.user,
                    content=data['content'],
                    )
            return HttpResponseRedirect(reverse('homepage'))
        form = CommentForm()
        return render(request, html, {'form': form})


def appetizer_filter(request):
    html = 'appetizer.html'
    appetizer =  Recipe.objects.filter(category='Appetizer')
    return render(request, html, {'appetizer': appetizer})


def breakfast_filter(request):
    html = 'breakfast.html'
    breakfast =  Recipe.objects.filter(category='Breakfast')
    return render(request, html, {'breakfast': breakfast})


def brunch_filter(request):
    html = 'brunch.html'
    brunch =  Recipe.objects.filter(category='Brunch')
    return render(request, html, {'brunch': brunch})


def lunch_filter(request):
    html = 'lunch.html'
    lunch =  Recipe.objects.filter(category='Lunch')
    return render(request, html, {'lunch': lunch})


def dinner_filter(request):
    html = 'dinner.html'
    dinner =  Recipe.objects.filter(category='Dinner')
    return render(request, html, {'dinner': dinner})

def dessert_filter(request):
    html = 'dessert.html'
    dessert =  Recipe.objects.filter(category='Dessert')
    return render(request, html, {'dessert': dessert})

@login_required
def recipe_upvote(request, id):
    html = "recipeview.html"
    try:
        vote = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    vote.total += 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def comment_upvote(request, id):
    html = "recipeview.html"
    try:
        vote = Comment.objects.get(id=id)
    except Comment.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    vote.total += 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def recipe_downvote(request, id):
    html = "recipeview.html"
    try:
        vote = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    vote.total -= 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def comment_downvote(request, id):
    html = "recipeview.html"
    try:
        vote = Comment.objects.get(id=id)
    except Comment.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    vote.total -= 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage'))

