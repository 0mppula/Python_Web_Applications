""" Defines URL's for blogs. """

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Add a new blog
    path('new_blog/', views.new_blog, name='new_blog'),
]