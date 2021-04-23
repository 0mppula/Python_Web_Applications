""" Models for blogs. """
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """ A blog that contains a title, text and the date of entry. """
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        """ Return a string representation of the model. """
        return self.title
