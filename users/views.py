from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import LoginForm, SignInForm


def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_entry = form.cleaned_data['login']
            password = form.cleaned_data['password']
            if "@" in login_entry:
                username = User.objects.get(email=login_entry).username
                user = authenticate(request, username=username, password=password)
            else:
                user = authenticate(request, username=login_entry, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.add_message(
                    request, messages.ERROR,
                    message="Access denied: wrong password", extra_tags="danger")
        else:
            return render(request, "users/login.html", {'form':form})

    form = LoginForm()
    return render(request, "users/login.html", {'form':form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def account(request):
    return render(request, "users/account.html")


def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')
        else:
            return render(request, "users/signin.html", {'form':form})

    form = SignInForm()
    return render(request, "users/signin.html", {'form':form})