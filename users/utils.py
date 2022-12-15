from django.conf import settings
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.template.loader import get_template


def send_password_reset_email(request, user):
    token = user.get_jwt_token(expires_in=600)
    domain = request.build_absolute_uri('/')[:-1]
    link = domain + reverse('reset_password', args=[token])
    context = {
        'user': user,
        'link': link
    }

    msg_text = get_template("users/email/request_password_reset.txt")
    send_mail(
        'Password reset request',
        msg_text.render(context),
        'from@example.com',
        [user.email],
        fail_silently=False,
    )


def send_confirm_email(request, user):
    token = user.get_jwt_token(expires_in=600)
    domain = request.build_absolute_uri('/')[:-1]
    link = domain + reverse('confirm_email', args=[token])
    context = {
        'user': user,
        'link': link
    }

    msg_text = get_template("users/email/confirm_email.txt")
    send_mail(
        'Confirm your new email',
        msg_text.render(context),
        'from@example.com',
        [user.unconfirmed_email],
        fail_silently=False,
    )