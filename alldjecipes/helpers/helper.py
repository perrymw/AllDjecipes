from alldjecipes.recipes.models import Recipe, Comment
from alldjecipes.recipes.forms import CommentForm, RecipeForm

def voting_helper(id, model, vote_type):
    vote = model.objects.get(id=id)
    if vote_type == 'upvote':
        vote.total += 1
    elif vote_type == 'downvote':
        vote.total -= 1
    vote.save()
    return vote