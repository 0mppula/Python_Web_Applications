from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate

from .forms import UserCreateForm

def logout_view(request):
    """ Logout user. """
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

def login_view(request):
    """ Logout user. """
    return HttpResponseRedirect(reverse('blogs:index'))

def register(request):
    """ Register a new user. """
    if request.method != 'POST':
        # Display blank registeration form
        form = UserCreateForm()
    else:
        # Process completed form
        form = UserCreateForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        # Log the user in and redirect to home page
        authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)