from django import forms
from alldjecipes.users.models import ChefUser

class SignupForm(forms.ModelForm):
    class Meta:
        model = ChefUser
        fields = (
            'firstname',
            'lastname',
            'email',
            'username',
            'password',
        )
