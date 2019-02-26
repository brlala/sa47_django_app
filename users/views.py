from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # this will convert the form data to python readable types
            username = form.cleaned_data.get('username')

            # this will show a flash message on success
            messages.success(request, f'Account created for {username}!')
            return redirect('mysite-home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
