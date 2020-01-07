from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from alldjecipes.recipes import views



urlpatterns = [
    path('addrecipe/', views.AddRecipe.as_view(), name='addrecipe')
    ]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 