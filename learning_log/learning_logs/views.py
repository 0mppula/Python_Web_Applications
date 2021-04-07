from django.shortcuts import render


def index(request):
    """ The homepage for learning Log.  """
    return render(request, 'learning_logs/index.html')
