from django.shortcuts import render


def index(request):
    """ The homepage for pizzas app. """
    return render(request, 'pizzas/index.html')
