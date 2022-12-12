from django import forms
from django.forms import ValidationError
from django.core.validators import (
    EmailValidator,
    MinLengthValidator,
    MaxLengthValidator
)
from .models import User


class LoginForm(forms.Form):
    login = forms.CharField(
        max_length=64,
        widget=forms.TextInput({'placeholder':'username or email'})
    )
    password = forms.CharField(
        max_length=64, widget=forms.PasswordInput,
        validators=[MinLengthValidator(4), MaxLengthValidator(64)]
    )

    def clean_login(self):
        login = self.cleaned_data['login']
        if "@" in login:
            user = User.objects.filter(email=login)
        else:
            user = User.objects.filter(username=login)
        if not user or not user[0].is_active:
            raise ValidationError(f"user '{login}' unknown or unconfirmed")
        return login


class SignInForm(forms.Form):
    username = forms.CharField(
        validators=[MinLengthValidator(4), MaxLengthValidator(64)],
        max_length=64,
    )
    email = forms.EmailField(validators=[EmailValidator()])

    def clean_username(self):
        username = self.cleaned_data['username']
        if "@" in username:
            raise ValidationError("'@' not allowed in a username")
        else:
            user = User.objects.filter(username=username)
            if user:
                raise ValidationError(f"'{username}' already used by someone")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user:
            raise ValidationError(f"'{email}' already used.")
        return email


class RequestPasswordResetForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator()])

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if not user:
            raise ValidationError(f"'{email}' unknown or unconfirmed")
        return email


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        max_length=64, widget=forms.PasswordInput,
        validators=[MinLengthValidator(4), MaxLengthValidator(64)]
    )
    password2 = forms.CharField(
        label="Confirm password",
        max_length=64, widget=forms.PasswordInput,
        validators=[MinLengthValidator(4), MaxLengthValidator(64)]
    )

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError("different than password")
        return password2


class ChangeUsernameForm(forms.Form):
    username = forms.CharField(
        validators=[MinLengthValidator(4), MaxLengthValidator(64)],
        max_length=64,
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if "@" in username:
            raise ValidationError("'@' not allowed in a username")
        else:
            user = User.objects.filter(username=username)
            if user:
                raise ValidationError(f"'{username}' already used by someone")
        return username


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(
        label="New e-mail address",
        validators=[EmailValidator()]
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user:
            raise ValidationError(f"'{email}' already used by someone")
        return email
