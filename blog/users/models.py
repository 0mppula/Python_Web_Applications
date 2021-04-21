from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreateForm(UserCreationForm):
    """ Create a user registration form with no help text. """
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
