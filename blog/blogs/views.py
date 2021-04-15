from django.shortcuts import render

def index(request):
    """ The home page for blogs. """
    return render(request, 'blogs/index.html')
