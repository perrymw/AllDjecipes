from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import View
from alldjecipes.users.forms import SignupForm
from alldjecipes.users.models import ChefUser

class AddUser(View):
    html = 'generic_form.html'
    def get(self, request):
        form = SignupForm()
        return render(request, self.html, {'form': form})
    def post(self, request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_recipe = ChefUser.objects.create(
                    firstname=data['firstname'],
                    lastname=data['lastname'],
                    email=data['email'],
                    username=data['username'],
                    password=data['password'],
                )
            return HttpResponseRedirect(reverse('homepage'))
        form = SignupForm()
        return render(request, html, {'form': form})