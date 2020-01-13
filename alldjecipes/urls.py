"""alldjecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alldjecipes.users.models import ChefUser
from alldjecipes.recipes.models import Comment,Recipe, Vote
from alldjecipes.authentication.urls import urlpatterns as auth_urls
from alldjecipes.recipes.urls import urlpatterns as recipe_urls
from alldjecipes.users.urls import urlpatterns as users_urls


admin.site.register(ChefUser)
admin.site.register(Comment)
admin.site.register(Recipe)
admin.site.register(Vote)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += auth_urls
urlpatterns += recipe_urls
urlpatterns += users_urls