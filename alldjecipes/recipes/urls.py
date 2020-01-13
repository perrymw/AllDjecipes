from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from alldjecipes.recipes import views



urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe'),
    path('addrecipe/', views.AddRecipe.as_view(), name='addrecipe'),
    path('recipeupvote/<int:id>', views.recipe_upvote, name=''),
    path('commentdownvote/<int:id>', views.recipe_downvote, name=''),
    path('commentupvote/<int:id>', views.comment_upvote, name=''),
    path('commentdownvote/<int:id>', views.comment_downvote, name=''),
    path('<int:id>/addcomment/', views.AddComment.as_view(), name='addcomment'),
    path('category/<str:param>/',views.filter_by_category),
    ]
# https://www.geeksforgeeks.org/python-uploading-images-in-django/
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 