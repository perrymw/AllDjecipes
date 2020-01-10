from django.contrib.auth import login, logout, authenticate
from alldjecipes.users.models import ChefUser
from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from alldjecipes.authentication.forms import LoginForm



def login_view(request):
    html = "generic_form.html"

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if user := authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))