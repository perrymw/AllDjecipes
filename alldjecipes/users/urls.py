from django.contrib import admin
from django.urls import path
from alldjecipes.recipes.views import index
from alldjecipes.users import views

urlpatterns = [
    path('', index, name='homepage'),
    path('adduser/', views.AddUser.as_view(), name="adduser"),
    path('users/', views.all_users_view,),
    path('chefuser/<int:id>/', views.user_view, name='chefuser')
]