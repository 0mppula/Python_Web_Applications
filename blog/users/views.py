from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    """ Logout user. """
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

