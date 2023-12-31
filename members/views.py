from django.shortcuts import render, redirect
# User Authentification
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('view_tasks')
        else:
            messages.error(
                request, "There was an error logging in. Please try again."
                )
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

# Logging out


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('home')

# Register User


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, ('You have successfully signed up to Task Pro'))
            return redirect('view_tasks')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form': form})
