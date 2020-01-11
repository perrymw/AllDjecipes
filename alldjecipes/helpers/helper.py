from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from alldjecipes.recipes.forms import CommentForm, RecipeForm



def _upvote(request, id, source):
    html = "recipeview.html"
    try:
        vote = source.objects.get(id=id)
    except source.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    vote.total += 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage'))

    
def _downvote(request, id, source):
    html = "recipeview.html"
    try:
        vote = source.objects.get(id=id)
    except source.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    vote.total -= 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage'))