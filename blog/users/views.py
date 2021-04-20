from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """ Logout user. """
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

def register(request):
    """ Register a new user. """
    if request.method != 'POST':
        # Display blank registeration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        print(f'New user: {new_user}')
        # Log the user in and redirect to home page
        authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
        print(f'Authenticated user: {authenticated_user}')
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)