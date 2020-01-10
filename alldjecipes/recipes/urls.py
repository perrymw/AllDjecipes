from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from alldjecipes.recipes import views



urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<int:id>/', views.recipe_detail),
    path('addrecipe/', views.AddRecipe.as_view(), name='addrecipe'),
    path('<int:id>/addcomment/', views.AddComment.as_view(), name='addcomment'),
    ]
# https://www.geeksforgeeks.org/python-uploading-images-in-django/
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 