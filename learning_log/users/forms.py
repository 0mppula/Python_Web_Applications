from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    """ Create a user registeration form without any help text. """

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None