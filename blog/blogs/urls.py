""" Defines URL's for blogs. """

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Add a new blog
    path('new_blog/', views.new_blog, name='new_blog'),
    # Edit a blog
    path('edit_blog/<int:blog_id>/' , views.edit_blog, name='edit_blog'),
    # Delete a blog
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]