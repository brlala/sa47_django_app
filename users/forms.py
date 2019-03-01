from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta class is a nested namespace for configuration, the model 'User' will be affected when we use the command form.save() and the fields that we have is the fields we want to include in the form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# User update form will allow us to update user and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # Meta class is a nested namespace for configuration, the model 'User' will be affected when we use the command form.save() and the fields that we have is the fields we want to include in the form
    class Meta:
        model = User
        fields = ['username', 'email']


# Profile update form will allow us to update our image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
