from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import (
    LoginForm,
    SignInForm,
    RequestPasswordResetForm,
    ResetPasswordForm,
    ChangeUsernameForm,
    ChangeEmailForm,
)
from .utils import send_password_reset_email, send_confirm_email


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
                user = authenticate(
                    request, username=username, password=password)
            else:
                user = authenticate(
                    request, username=login_entry, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.add_message(
                    request, messages.ERROR,
                    message="Access denied: wrong password",
                    extra_tags="danger")
        else:
            return render(request, "users/login.html", {'form': form})

    form = LoginForm()
    return render(request, "users/login.html", {'form': form})


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
            user = User(username=username, email=email, is_active=False)
            user.save()
            messages.add_message(
                request, messages.INFO,
                message=(
                    f"Please check your email '{email}' to "
                    "confirm your account and set your password"
                    ),
                extra_tags="info"
            )
            send_password_reset_email(request, user)
            return redirect('login')
        else:
            return render(request, "users/signin.html", {'form': form})

    form = SignInForm()
    return render(request, "users/signin.html", {'form': form})


def request_password_reset(request):
    if request.method == "POST":
        form = RequestPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            send_password_reset_email(request, user)

            messages.add_message(
                request, messages.INFO,
                message=(
                    f"Please check your email '{email}' "
                    "to reset your password"
                    ),
                extra_tags="info"
            )
        else:
            return render(
                request,
                "users/request_password_reset.html",
                {'form': form}
                )
    form = RequestPasswordResetForm()
    if request.user.is_authenticated:
        form = RequestPasswordResetForm(initial={'email': request.user.email})
    return render(request, "users/request_password_reset.html", {'form': form})


def reset_password(request, token):
    user = User.verify_token(token)
    if user is None:
        return HttpResponse("Token invalid or expired")

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(
                request, messages.SUCCESS,
                message="Your password have been reset",
                extra_tags="success"
            )
            return redirect('account')
        else:
            return render(request, "users/reset_password.html", {'form': form})
    form = ResetPasswordForm()
    context = {
        'user': user,
        'form': form,
    }
    return render(request, "users/reset_password.html", context)


@login_required
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = request.user
            user.username = username
            user.save()
            messages.add_message(
                request, messages.SUCCESS,
                message=f"New username set: '{username}'",
                extra_tags="success"
            )
            return redirect("account")
        else:
            return render(
                request,
                "users/change_username.html",
                {'form': form},
                )

    form = ChangeUsernameForm()
    return render(request, "users/change_username.html", {'form': form})


@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = request.user
            user.unconfirmed_email = email
            user.save()
            send_confirm_email(request, user)

            messages.add_message(
                request, messages.INFO,
                message=(
                    "Please check your email to"
                    f" confirm your address '{email}'"
                    ),
                extra_tags="info"
            )
        else:
            return render(request, "users/change_email.html", {'form': form})

    form = ChangeEmailForm()
    return render(request, "users/change_email.html", {'form': form})


def confirm_email(request, token):
    user = User.verify_token(token)
    if user is not None:
        user.email = user.unconfirmed_email
        user.unconfirmed_email = None
        user.save()
        login(request, user)
        messages.add_message(
            request, messages.SUCCESS,
            message=f"Your new email have been confirmed: '{user.email}'",
            extra_tags="success"
        )

        return redirect("account")
