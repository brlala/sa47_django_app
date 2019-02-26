from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta class is a nested namespace for configuration, the model 'User' will be affected when we use the command form.save() and the fields that we have is the fields we want to include in the form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
