from django.db import forms
from alldjecipes.users.models import ChefUser

class SignupForm(forms.ModelForm):
    class Meta:
        model = ChefUser
        fields = [
            'First Name',
            'Last Name',
            'Email Address'
            'Username',
            'Password',
        ]
