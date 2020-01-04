from django import forms
from alldjecipes.users.models import ChefUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)