from django.shortcuts import render

from .models import BlogPost

def index(request):
    """ The home page for blogs also displays all blogs. """
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)
