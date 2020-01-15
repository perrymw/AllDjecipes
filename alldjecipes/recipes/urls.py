from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from alldjecipes.recipes import views
from alldjecipes.users.views import *



urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('addrecipe/', views.AddRecipe.as_view(), name='addrecipe'),
    path('editrecipe/<int:id>/', views.edit_recipe_view, name='editrecipe'),
    path('chefuser/<int:id>/', user_view, name='chefuser'),
    path('recipeupvote/<int:id>/', views.recipe_upvote),
    path('recipedownvote/<int:id>/', views.recipe_downvote),
    path('commentupvote/<int:id>/', views.comment_upvote),
    path('commentdownvote/<int:id>/', views.comment_downvote),
    path('<int:id>/addcomment/', views.AddComment.as_view(), name='addcomment'),
    path('category/<str:param>/',views.filter_by_category),
    ]
# https://www.geeksforgeeks.org/python-uploading-images-in-django/
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 